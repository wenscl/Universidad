using System;
using System.Collections.Generic;
using System.Text;

namespace Sokoban
{
    public delegate void FinJuego(int CantidadAcciones);

    public class Juego
    {

        #region Properties

        private Dictionary<Posicion, Casilla> _casillas;
        public Dictionary<Posicion, Casilla> casillas
        {
            get { return _casillas; }
            set { _casillas = value; }
        }

        public bool JuegoFinalizado
        {
            get 
            {
                //El juego tiene solucion cuando no hay casillas de meta sin una caja encima            
                foreach (Casilla cas in this.casillas.Values)
                {
                    if (cas.esMeta && !cas.ContieneCaja)
                    {
                        return false;
                    }
                }
                return true;
            }
        }

        private Personaje _personaje;
        public Personaje personaje
        {
            get { return _personaje; }
            set { _personaje = value; }
        }

        int _CantidadFilas;
        public int CantidadFilas 
        {
            get { return _CantidadFilas; }
        }

        int _CantidadColumnas;
        public int CantidadColumnas 
        {
            get { return _CantidadColumnas; } 
        }

        #endregion

        private int cant;
        public Juego(int CantidadFilas, int CantidadColumnas)
        {
            casillas = new Dictionary<Posicion, Casilla>();
            //cargamos las casillas vacias
            Casilla c;
            for (int x = 0; x < CantidadColumnas; x++)
            {
                for (int y = 0; y < CantidadFilas; y++)
                {
                    c = new Casilla(x, y);
                    this.casillas.Add(c.posicion, c);
                }
            }
            _CantidadColumnas = CantidadColumnas;
            _CantidadFilas = CantidadFilas;

            cant = 0;
        }

        public void HacerAccion(TipoAccion accion)
        {
            Casilla sigCasilla = obtenerSiguienteCasilla(accion, personaje.casilla);
            if (sigCasilla != null)
            {
                cant += 1;
                if (sigCasilla.EstaVacia)
                {
                    personaje.casilla = sigCasilla;
                }
                else if (sigCasilla.ContieneCaja)
                {
                    //ver si podemos empujar la caja. Para eso la casilla que sigue de la caja tiene que estar vacia
                    Casilla sig_caja = obtenerSiguienteCasilla(accion, sigCasilla);
                    if (sig_caja != null && sig_caja.EstaVacia)
                    {
                        //movemos la caja y el personaje
                        sigCasilla.objetoQueContiene.casilla = sig_caja;
                        personaje.casilla = sigCasilla;
                    }
                }
            }
        }

        public Casilla ObtenerCasilla(int x, int y)
        {
            return this.casillas[new Posicion(x, y)];
        }

        private Casilla obtenerSiguienteCasilla(TipoAccion accion, Casilla casillaActual)
        {
            Posicion posActual = casillaActual.posicion;
            Posicion sig = new Posicion (posActual.x, posActual.y);
            switch (accion)
            {
                case TipoAccion.Abajo :
                    sig.y--;
                    break;
                case TipoAccion.Arriba:
                    sig.y++;
                    break;
                case TipoAccion.Derecha:
                    sig.x++;
                    break;
                case TipoAccion.Izquierda:
                    sig.x--;
                    break;
            }

            if (casillas.ContainsKey(sig))
                return this.casillas[sig];
            return null;
        }
    }
}
