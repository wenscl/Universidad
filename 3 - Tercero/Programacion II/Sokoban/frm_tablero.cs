using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace Sokoban
{
    public partial class frm_tablero : Form
    {
        Juego _un_juego;
        public frm_tablero()
        {
            InitializeComponent();
            GeneradorNiveles generador = new GeneradorNiveles();
            _un_juego = generador.GenerarNivel(1);
            this.sokobanCtrl1.Juego = _un_juego;
        }

        private void frm_tablero_Load(object sender, EventArgs e)
        {
        }

        private void frm_tablero_KeyUp(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Up)
                _un_juego.HacerAccion(TipoAccion.Arriba);
            else if (e.KeyCode == Keys.Down)
                _un_juego.HacerAccion(TipoAccion.Abajo);
            else if (e.KeyCode == Keys.Left)
                _un_juego.HacerAccion(TipoAccion.Izquierda);
            else if (e.KeyCode == Keys.Right)
                _un_juego.HacerAccion(TipoAccion.Derecha);

            //this.sokobanCtrl1.Redibujar();
        }

    }
}
