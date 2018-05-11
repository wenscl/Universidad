using System;
using System.Collections.Generic;
using System.Text;

namespace Sokoban
{
    class GeneradorNiveles
    {
        public Juego GenerarNivel(int Nivel)
        {
            Juego res=null;
            if (Nivel == 1)
            {
                res = new Juego(6, 9);

                //marcamos las paredes
                Pared p;
                for (int x = 0; x < 9; x++)
                {
                    //agrega las paredes del piso
                    p = new Pared();
                    p.casilla = res.ObtenerCasilla(x, 0);
                    //agrega paredes en el techo
                    p = new Pared();
                    p.casilla = res.ObtenerCasilla(x, 5);
                    //agrega paredes en la linea inferior al techo
                    if (x != 3 && x != 4)
                    {
                        p = new Pared();
                        p.casilla = res.ObtenerCasilla(x, 4);
                    }
                }
                for (int y = 1; y < 4; y++)
                {
                    //agrega pared izquierda
                    p = new Pared();
                    p.casilla = res.ObtenerCasilla(0, y);
                    //agrega pared derecha
                    p = new Pared();
                    p.casilla = res.ObtenerCasilla(8, y);
                }

                //agrega las paredes que faltan
                p = new Pared();
                p.casilla = res.ObtenerCasilla(2, 2);
                p = new Pared();
                p.casilla = res.ObtenerCasilla(5, 1);
                p = new Pared();
                p.casilla = res.ObtenerCasilla(5, 2);

                //ahora marcamos las meta
                res.ObtenerCasilla(2, 1).esMeta = true;
                res.ObtenerCasilla(4, 1).esMeta = true;

                //agregamos las cajas
                Caja caja;
                caja = new Caja();
                caja.casilla = res.ObtenerCasilla(6, 2);
                caja = new Caja();
                caja.casilla = res.ObtenerCasilla(6, 3);

                //agregamos el personaje
                Personaje per = new Personaje();
                per.casilla = res.ObtenerCasilla(6, 1);
                res.personaje = per;
            }
            return res;
        }
    }
}
