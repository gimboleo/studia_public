function Tree(val, left, right)
{
    this.val = val
    this.left = left
    this.right = right
}


/*
//Recursive DFS
Tree.prototype[Symbol.iterator] = function*()
{
    yield this.val
    if (this.left) yield* this.left
    if (this.right) yield* this.right
}
*/


//Queue - BFS
Tree.prototype[Symbol.iterator] = function*()
{
    let queue = [this]

    while (queue.length)
    {
        let x = queue.shift()
        if (x.left) queue.push(x.left)
        if (x.right) queue.push(x.right)
        yield x.val
    }
}


/*
//Stack - DFS
Tree.prototype[Symbol.iterator] = function*()
{
    let stack = [this]

    while (stack.length)
    {
        let x = stack.pop()
        if (x.left) stack.push(x.left)
        if (x.right) stack.push(x.right)
        yield x.val
    }
}
*/


let root = new Tree(1, new Tree(2, new Tree(3)), new Tree(4))

for (let e of root) console.log(e)