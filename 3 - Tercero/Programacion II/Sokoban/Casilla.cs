using System;
using System.Collections.Generic;
using System.Text;

namespace Sokoban
{
    public delegate void CambioCasillaDelegate(Casilla sender);

    public class Casilla
    {
        public event CambioCasillaDelegate OnCambioCasilla;

        private Posicion  _posicion;
        public Posicion  posicion
        {
            get { return _posicion; }
            set { _posicion = value; }
        }

        private bool _esMeta;
        public bool esMeta
        {
            get { return _esMeta; }
            set { _esMeta = value; }
        }

        private ObjetoContenible  _objetoQueContiene;
        public ObjetoContenible  objetoQueContiene
        {
            get { return _objetoQueContiene; }
            set 
            { 
                _objetoQueContiene = value;
                if (OnCambioCasilla != null)
                    OnCambioCasilla(this);
            }
        }

        public bool EstaVacia
        {
            get { return objetoQueContiene == null; }
        }

        public bool ContieneCaja
        {
            get { return !EstaVacia && objetoQueContiene.GetType() == typeof(Caja); }
        }

        public Casilla(Posicion pos, bool meta)
        {
            posicion = pos;
            esMeta = meta;
        }

        public Casilla(int x, int y)
        {
            posicion = new Posicion(x, y);
            esMeta = false;
        }

    }
}
