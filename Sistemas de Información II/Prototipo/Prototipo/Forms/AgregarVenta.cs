using Prototipo.Class;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Prototipo.Forms
{
    public partial class AgregarVenta : Form
    {
        public AgregarVenta()
        {
            InitializeComponent();
        }

        private void AgregarVenta_Load(object sender, EventArgs e)
        {
            Ventas.DataSource = Venta.Listar();
        }

        private void Agregar_Click(object sender, EventArgs e)
        {
            var venta = new Venta();

            venta.Fecha = DateTime.Now;
            venta.Total = 0;

            Venta.Agregar(venta);

            Ventas.DataSource = Venta.Listar();
            
            txtCantidad.Enabled = true;
            txtProducto.Enabled = true;
            Siguiente.Enabled = true;
            Terminar.Enabled = true;
            txtPrecio.Enabled = true;
        }

        private void Eliminar_Click(object sender, EventArgs e)
        {
            if (Ventas.SelectedRows.Count > 0)
            {
                var id = Ventas.SelectedRows[0].Cells["Id"].Value.ToString();
                Venta.Eliminar(Convert.ToInt32(id));
                Ventas.DataSource = Venta.Listar();
            }
        }

        private void Modificar_Click(object sender, EventArgs e)
        {

        }

        public float total { get; set; }

        private void Siguiente_Click(object sender, EventArgs e)
        {
            var detalle = new DetalleVenta();
            Ventas.Rows[Ventas.Rows.Count - 1].Selected = true;
            int id = Convert.ToInt32(Ventas.SelectedRows[0].Cells["Id"].Value);
            detalle.IdVenta = id;
            //detalle.IdVenta = Ventas.Rows.Count - 1;
            detalle.CodigoProducto = txtProducto.Text;
            detalle.Cantidad = Convert.ToInt32(txtCantidad.Text);
            detalle.Precio = Convert.ToSingle(txtPrecio.Text);
            total += Convert.ToSingle(txtPrecio.Text);
            DetalleVenta.Agregar(detalle);

            //Detalle.DataSource = DetalleVenta.Todos();
            Detalle.DataSource = DetalleVenta.Todos();
            //Detalle.Refresh();
        }

        private void Terminar_Click(object sender, EventArgs e)
        {
            txtCantidad.Enabled = false;
            txtProducto.Enabled = false;
            Siguiente.Enabled = false;
            Terminar.Enabled = false; 
            txtPrecio.Enabled = false;

            var venta = new Venta();
            Ventas.Rows[Ventas.Rows.Count - 1].Selected = true;
            venta.Id = Convert.ToInt32(Ventas.SelectedRows[0].Cells["Id"].Value);
            //venta.Id = Ventas.Rows.Count - 1;
            venta.Fecha = DateTime.Now;
            venta.Total = total;
            Venta.Modificar(venta);

            Ventas.DataSource = Venta.Listar();

            total = 0;
        }

        private void VerDetalle_Click(object sender, EventArgs e)
        {
            if (Ventas.SelectedRows.Count > 0)
            {
                var id = Convert.ToInt32(Ventas.SelectedRows[0].Cells["Id"].Value);
                Detalle.DataSource = DetalleVenta.Listar(id);
            }
        }
    }
}
