#Sources:
# Whitebook for the 'Logic for Computer Science' course
# https://en.wikipedia.org/wiki/Propositional_formula



from abc import ABC, abstractmethod
from itertools import combinations_with_replacement as cwr



class WrongTypeError(Exception):
    'Exception for when the user provides an argument that is not derived from the Formula class'


    def __init__(self, arg):
        self.arg = arg
        super().__init__()


    def __str__(self): return f'{self.arg} is not of class Formula!'



class FreeVariableError(Exception):
    'Exception for when the formula cannot be evaluated due to a free variable'


    def __init__(self, v):
        self.v = v
        super().__init__()


    def __str__(self): return f'Variable {self.v} is unassigned!'


#Inheriting from ABC makes this class abstract
class Formula(ABC):
    'Abstract class that all formula types inherit from'

    #Priority table created to avoid printing out needless parentheses in the __str__ method
    #If a given subformula has lower priority (bigger number) than its parent, it needs to be wrapped in parentheses
    #(lower of equal for the left side of implication)
    priorities = {
        'Constant': 1, 
        'Variable': 1, 
        'Not': 2,
        'And': 3,
        'Or': 4,
        'Imply': 5,
        'Equiv': 6
    }


    #I assume that the variables will be provided in a dictionary with strings representing variables as keys and
    #data that is castable into boolean as their values
    @abstractmethod
    def evaluate(self, variables = {}): pass


    @abstractmethod
    def __str__(self): pass


    def __add__(self, other):
        if not isinstance(other, Formula): raise WrongTypeError(other)
        return Or(self, other)


    def __mul__(self, other):
        if not isinstance(other, Formula): raise WrongTypeError(other)
        return And(self, other)


    def __eq__(self, other): 
        '''
        This method is NOT for checking equivalence - it checks for strict equality¹ and is used in the simplify(formula) function
        
        ¹Well, not exactly strict, as it treats binop(l, r) and binop(r, l) as equal for symmetrical binops
        '''

        if not isinstance(other, Formula): raise WrongTypeError(other)
        if type(self) is not type(other): return False
        #Checks if both objects have the same attributes; it's sufficient for the simple classes (Constant, Variable)
        if self.__dict__ == other.__dict__: return True
        
        if isinstance(self, Unop): return self.val == other.val
        #Implication is not symmetrical so it's checked separately!
        if isinstance(self, Imply): return (self.l == other.l and self.r == other.r) 
        if isinstance(self, Binop): return (self.l == other.l and self.r == other.r) or (self.l == other.r and self.r == other.l)
        return False


    @staticmethod
    def tautology(formula):
        def aux(f):
            'This function returns a set containing names of all the variables inside a given formula'
            if isinstance(f, Constant): return set()
            if isinstance(f, Variable): return {f.val}
            if isinstance(f, Unop): return aux(f.val)
            if isinstance(f, Binop): return aux(f.l) | aux(f.r)
            return set()

        if not isinstance(formula, Formula): raise WrongTypeError(formula)
        
        variables = aux(formula)

        #Basically we check if the formula is True for all possible assignments of its variables
        combinations = [dict(zip(variables, v)) for v in cwr([True, False], len(variables))]
        return all(formula.evaluate(var) for var in combinations)


    @staticmethod
    def simplify(formula):
        '''
        A function that returns a slightly simplified formula. Of course it does not simplify everything that can be simplified
        in propositional logic - it follows a few chosen rules
        '''

        if not isinstance(formula, Formula): raise WrongTypeError(formula)
        
        #Firstly we simplify the subformulas, then try to simplify the parent formula
        if isinstance(formula, Unop):
            aux = Formula.simplify(formula.val)

            if isinstance(formula, Not):
                #¬¬a = a
                if isinstance(aux, Not): return aux.val
                #¬T = F; ¬F = T
                if isinstance(aux, Constant): return Constant(not aux.val)
            
            #If we didn't manage to simplify the parent formula, we return it unchanged, but with simplified children
            #type(object) returns the type of a given object, we can create a new object of the same type
            return type(formula)(aux)

        if isinstance(formula, Binop):
            la = Formula.simplify(formula.l)
            ra = Formula.simplify(formula.r)

            if isinstance(formula, Or):
                #(a ∨ F) = a
                if la == Constant(False): return ra
                if ra == Constant(False): return la

                #(a ∨ T) = T
                if la == Constant(True) or ra == Constant(True): return Constant(True)

                #(a ∨ ¬a) = T
                if isinstance(la, Not) and la.val == ra: return Constant(True)
                if isinstance(ra, Not) and ra.val == la: return Constant(True)

            if isinstance(formula, And):
                #(a Λ T) = a
                if la == Constant(True): return ra
                if ra == Constant(True): return la

                #(a Λ F) = F
                if la == Constant(False) or ra == Constant(False): return Constant(False)

                #(a Λ ¬a) = F
                if isinstance(la, Not) and la.val == ra: return Constant(False)
                if isinstance(ra, Not) and ra.val == la: return Constant(False)

            #binop(a, a) = a (implication doesn't apply)
            if not isinstance(formula, Imply) and la == ra: return la

            return type(formula)(la, ra)

        #No changes applied, basically a case for Variable and Constant classes
        return formula



class Unop(Formula):
    'An abstract class that all possible unary operators inherit from'

    @abstractmethod
    def __init__(self, formula):
        if not isinstance(formula, Formula): raise WrongTypeError(formula)
        self.val = formula



class Binop(Formula):
    'An abstract class that all possible binary operators inherit from'


    @abstractmethod
    def __init__(self, left, right):
        if not isinstance(left, Formula): raise WrongTypeError(left) 
        if not isinstance(right, Formula): raise WrongTypeError(right)
        self.l = left
        self.r = right



class Constant(Formula):
    #Given value will be cast to boolean - it doesn't have to be explicitly boolean
    def __init__(self, value): self.val = True if value else False

    def evaluate(self, variables = {}): return self.val

    def __str__(self): return str(self.val)



class Variable(Formula):
    def __init__(self, name): self.val = str(name)

    def evaluate(self, variables = {}):
        if self.val not in variables: raise FreeVariableError(self.val)
        return bool(variables[self.val])

    def __str__(self): return self.val



class Not(Unop):
    def __init__(self, formula): super().__init__(formula)

    def evaluate(self, variables = {}): return not self.val.evaluate(variables)

    def __str__(self):
        return f'¬({self.val})' if self.priorities[type(self).__name__] < self.priorities[type(self.val).__name__] else f'¬{self.val}'



class And(Binop):
    def __init__(self, left, right): super().__init__(left, right)

    def evaluate(self, variables = {}): return self.l.evaluate(variables) and self.r.evaluate(variables)

    def __str__(self):
        ls = f'({self.l})' if self.priorities[type(self).__name__] < self.priorities[type(self.l).__name__] else str(self.l)
        rs = f'({self.r})' if self.priorities[type(self).__name__] < self.priorities[type(self.r).__name__] else str(self.r)
        return ls + ' Λ ' + rs



class Or(Binop):
    def __init__(self, left, right): super().__init__(left, right)

    def evaluate(self, variables = {}): return self.l.evaluate(variables) or self.r.evaluate(variables)

    def __str__(self):
        ls = f'({self.l})' if self.priorities[type(self).__name__] < self.priorities[type(self.l).__name__] else str(self.l)
        rs = f'({self.r})' if self.priorities[type(self).__name__] < self.priorities[type(self.r).__name__] else str(self.r)
        return ls + ' V ' + rs



class Imply(Binop):
    def __init__(self, left, right): super().__init__(left, right)

    #a => b = ¬a V b
    def evaluate(self, variables = {}): return not self.l.evaluate(variables) or self.r.evaluate(variables)

    def __str__(self):
        ls = f'({self.l})' if self.priorities[type(self).__name__] <= self.priorities[type(self.l).__name__] else str(self.l)
        rs = f'({self.r})' if self.priorities[type(self).__name__] < self.priorities[type(self.r).__name__] else str(self.r)
        return ls + ' => ' + rs



class Equiv(Binop):
    def __init__(self, left, right): super().__init__(left, right)

    def evaluate(self, variables = {}): return self.l.evaluate(variables) == self.r.evaluate(variables)

    def __str__(self):
        ls = f'({self.l})' if self.priorities[type(self).__name__] < self.priorities[type(self.l).__name__] else str(self.l)
        rs = f'({self.r})' if self.priorities[type(self).__name__] < self.priorities[type(self.r).__name__] else str(self.r)
        return ls + ' <=> ' + rs



#TESTING ZONE#

x = Equiv(Not(Or(Variable('p'), Variable('q'))), And(Not(Variable('p')), Not(Variable('q'))))
print(x)
print(x.evaluate({'p': False, 'q': True}))
print(Formula.tautology(x))
print()

z = Or(Imply(Variable('s'), Variable('p')), And(Variable('p'), Variable('q')))
print(z)
print(z.evaluate({'p': False, 'q': True, 's': True}))
print(Formula.tautology(z))
print()

print(Imply(Variable('a'), Imply(Variable('a'), Variable('a'))))
print(Imply(Imply(Variable('a'), Variable('a')), Variable('a')))
print()

y = Constant(False)
print(x * y)
print(x + y)
print()

f = Equiv(And(Not(Variable('q')), Not(Variable('p'))), Not(Or(Variable('q'), Variable('p'))))
print(f)
print(f == x)
print(Imply(Constant(True), Constant(False)) == Imply(Constant(True), Constant(False)))
print(Imply(Constant(True), Constant(False)) == Imply(Constant(False), Constant(True)))
print()

try: b = Not(x for x in range(10))
except Exception as e: print(e)
try: x.evaluate()
except Exception as e: print(e)
try: x.evaluate({'p': False})
except Exception as e: print(e)
print()

simple = Not(Not(Not(Variable('x'))))
print(simple)
print(Formula.simplify(simple))
print()

simple = Not(simple)
print(simple)
print(Formula.simplify(simple))
print()

simple = Not(Not(Not(Constant(True))))
print(simple)
print(Formula.simplify(simple))
print()

simple = Or(Variable('a'), And(Variable('a'), Not(Variable('a'))))
print(simple)
print(Formula.simplify(simple))
print()

simple = Imply(Variable('a'), Imply(Variable('a'), And(Variable('a'), Or(Variable('a'), Variable('a')))))
print(simple)
print(Formula.simplify(simple))
print()