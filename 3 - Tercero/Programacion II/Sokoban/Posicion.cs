using System;
using System.Collections.Generic;
using System.Text;

namespace Sokoban
{
//definicion_basica
    public class Posicion
    {
        private Int32 _x;
        public Int32 x
        {
            get { return _x; }
            set { _x = value; }
        }

        private Int32 _y;
        public Int32 y
        {
            get { return _y; }
            set { _y = value; }
        }
    
        public Posicion(Int32 x, Int32 y)
        {
            this.x = x;
            this.y = y;
        }

        public static bool operator ==(Posicion xx, Posicion yy)
        {
            return xx.Equals(yy);
        }

        public static bool operator !=(Posicion xx, Posicion yy)
        {
            return !xx.Equals(yy);
        }


        public override bool Equals(object obj)
        {
            Posicion otro = (Posicion)obj;
            return this.x == otro.x && this.y == otro.y; 
        }

        public override int GetHashCode()
        {
            return this.x * 1000 + this.y;
        }
    }
}
