using System;
using System.Collections;

public class PrimeCollection: IEnumerable {
    public class PrimeEnumerator: IEnumerator {
        private int cur = -1;

        private bool IsPrime(int x) {
            if (x < 2) return false;
            if (x == 2) return true;

            int roof = System.Convert.ToInt32(Math.Ceiling(Math.Sqrt(x)));

            for (int i = 2; i<= roof; i++)
            {
                if (x % i == 0) return false;
            }
            return true;
        }

        private bool eos() {
            if (this.cur == Int32.MaxValue) return true;
            return false;
        }

        public PrimeEnumerator() {
            this.Reset();
        }

        public bool MoveNext() {
            this.cur++;

            while (!IsPrime(this.cur))
            {
                if(this.eos()) return false;
                this.cur++;
            }

            return true;
        }

        object IEnumerator.Current {
            get {return Current;}
        }

        public int Current
        {
            get {return this.cur;}
        }

        public void Reset()
        {
            this.cur = 1;
        }
    }

    IEnumerator IEnumerable.GetEnumerator() {
        return (IEnumerator) GetEnumerator();
    }

    public PrimeEnumerator GetEnumerator() {
        return new PrimeEnumerator();
    }
}