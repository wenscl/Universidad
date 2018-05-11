using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace JuegoCromy.Code
{
    public class Juego
    {
        public Juego() 
        {
            this.Partidas = new List<Partida>();
        }
        
        public IList<Partida> Partidas { get; set; }
    
        public void AgregarPartida(Partida partida)
        {
            if (Partidas.Where(x => x.Nombre == partida.Nombre).Count() == 0)
            { this.Partidas.Add(partida); }
            else
            { throw new ArgumentException("Ya existe una partida con ese nombre"); }
        }
    }
}
