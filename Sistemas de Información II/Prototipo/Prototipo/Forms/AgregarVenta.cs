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
            dataGridVentas.DataSource = Venta.Listar();
        }

        private void Agregar_Click(object sender, EventArgs e)
        {
            var venta = new Venta();
            venta.Fecha = DateTime.Now;
            venta.Total = 0;
            Venta.Agregar(venta);

            dataGridVentas.DataSource = Venta.Listar();
            
            txtCantidad.Enabled = true;
            txtProducto.Enabled = true;
            txtPrecio.Enabled = true;
            Siguiente.Enabled = true;
            Terminar.Enabled = true;
        }

        private void Eliminar_Click(object sender, EventArgs e)
        {
            if (dataGridVentas.SelectedRows.Count > 0)
            {
                var id = Convert.ToInt32(dataGridVentas.SelectedRows[0].Cells["Id"].Value);
                var lista = DetalleVenta.EliminarDetalle(id);
                foreach (DetalleVenta item in lista)
                {
                    DetalleVenta.Eliminar(item.IdVenta);
                }
                Venta.Eliminar(id);
                dataGridVentas.DataSource = Venta.Listar();
                dataGridDetalle.DataSource = DetalleVenta.Todos();
            }
        }

        private void Modificar_Click(object sender, EventArgs e)
        {

        }

        public float total { get; set; }

        private void Siguiente_Click(object sender, EventArgs e)
        {
            var detalle = new DetalleVenta();
            dataGridVentas.Rows[dataGridVentas.Rows.Count - 1].Selected = true;
            var id = Convert.ToInt32(dataGridVentas.SelectedRows[0].Cells["Id"].Value);
            detalle.IdVenta = id;
            //detalle.IdVenta = Ventas.Rows.Count - 1;
            detalle.CodigoProducto = txtProducto.Text;
            detalle.Cantidad = Convert.ToInt32(txtCantidad.Text);
            detalle.Precio = Convert.ToSingle(txtPrecio.Text);
            total += Convert.ToSingle(txtPrecio.Text);
            DetalleVenta.Agregar(detalle);
            
            dataGridDetalle.DataSource = DetalleVenta.Listar(id);
        }

        private void Terminar_Click(object sender, EventArgs e)
        {
            txtCantidad.Enabled = false;
            txtProducto.Enabled = false;
            txtPrecio.Enabled = false;
            Siguiente.Enabled = false;
            Terminar.Enabled = false;

            var venta = new Venta();
            dataGridVentas.Rows[dataGridVentas.Rows.Count - 1].Selected = true;
            venta.Id = Convert.ToInt32(dataGridVentas.SelectedRows[0].Cells["Id"].Value);
            venta.Fecha = DateTime.Now;
            venta.Total = total;
            Venta.Modificar(venta);

            dataGridVentas.DataSource = Venta.Listar();
            dataGridDetalle.DataSource = DetalleVenta.Todos();
            
            total = 0;
        }

        private void VerDetalle_Click(object sender, EventArgs e)
        {
            if (dataGridVentas.SelectedRows.Count > 0)
            {
                var id = Convert.ToInt32(dataGridVentas.SelectedRows[0].Cells["Id"].Value);
                dataGridDetalle.DataSource = DetalleVenta.Listar(id);
            }
        }
    }
}
