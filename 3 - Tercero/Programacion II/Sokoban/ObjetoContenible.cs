using System;
using System.Collections.Generic;
using System.Text;

namespace Sokoban
{
    public class ObjetoContenible
    {
        private Casilla _casilla;

        public Casilla casilla
        {
            get { return _casilla; }
            set 
            {
                if (_casilla != null) _casilla.objetoQueContiene = null;
                _casilla = value;
                _casilla.objetoQueContiene = this;
            }
        }


        private System.Drawing.Bitmap  _imagen;
        public System.Drawing.Bitmap  imagen
        {
            get { return _imagen; }
            set { _imagen = value; }
        }
	
	
    }
}
