using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Text;
using System.Windows.Forms;

namespace Sokoban
{
    public partial class SokobanCtrl : UserControl
    {
        public SokobanCtrl()
        {
            InitializeComponent();
        }

        private Juego _juego;

        public Juego Juego
        {
            get { return _juego; }
            set 
            { 
                _juego = value; 
                if (value != null) 
                {
                    InicializarJuego();
                }
            }
        }

        private void InicializarJuego()
        {
            //creo las columnas
            this.layout.RowCount = _juego.CantidadFilas + 1;
            this.layout.RowStyles.Clear();
            this.layout.RowStyles.Add(new RowStyle(SizeType.AutoSize));
            for (int i = 0; i < _juego.CantidadFilas; i++)
            {
                this.layout.RowStyles.Add(new RowStyle(SizeType.Absolute, 75));
            }

            //creo las filas
            this.layout.ColumnCount = _juego.CantidadColumnas + 1;
            this.layout.ColumnStyles.Clear();
            for (int i = 0; i < _juego.CantidadColumnas; i++)
            {
                this.layout.ColumnStyles.Add(new ColumnStyle(SizeType.Absolute, 75));
            }
            this.layout.ColumnStyles.Add(new ColumnStyle(SizeType.AutoSize));
            PictureBox pic;
            foreach (Casilla c in _juego.casillas.Values)
            {
                pic = new PictureBox();
                pic.Dock = DockStyle.Fill;
                pic.Margin = new Padding(0);
                this.layout.Controls.Add(pic, pos_x(c.posicion), pos_y(c.posicion));
                InvalidarCasilla(c);
                c.OnCambioCasilla += InvalidarCasilla;
            }
        }

        public void Redibujar()
        {
            foreach (Casilla c in _juego.casillas.Values)
            {
                InvalidarCasilla(c);
            }
        }

        private void InvalidarCasilla(Casilla c)
        {
            PictureBox pic = (PictureBox)this.layout.GetControlFromPosition(pos_x(c.posicion), pos_y(c.posicion));
            if (!c.EstaVacia)
                pic.Image = c.objetoQueContiene.imagen;
            else if (c.esMeta)
                pic.Image = Sokoban.Properties.Resources.meta;
            else
                pic.Image = null;
        }

        private int pos_x(Posicion pos)
        {
            return pos.x;
        }

        private int pos_y(Posicion pos)
        {
            return _juego.CantidadFilas - pos.y;
        }
    }
}
