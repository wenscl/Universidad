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
            dataGridDetalle.DataSource = DetalleVenta.Todos();
            txtCantidad.Enabled = false;
            txtProducto.Enabled = false;
            txtPrecio.Enabled = false;
            Siguiente.Enabled = false;
            Terminar.Enabled = false;
            Cancelar.Enabled = false;
            Modificar.Enabled = true;
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
            Cancelar.Enabled = true;
            Modificar.Enabled = false;
        }

        private void Eliminar_Click(object sender, EventArgs e)
        {
            if (dataGridVentas.SelectedRows.Count > 0)
            {
                var id = Convert.ToInt32(dataGridVentas.SelectedRows[0].Cells["Id"].Value);
                var lista = DetalleVenta.Listar(id);
                foreach (DetalleVenta item in lista)
                {
                    DetalleVenta.Eliminar(item.Id);
                }
                Venta.Eliminar(id);
                dataGridVentas.DataSource = Venta.Listar();
                dataGridDetalle.DataSource = DetalleVenta.Todos();
            }
        }

        private bool bandera = false;
        private float precio_anterior { get; set; }
        private float cantidad_anterior { get; set; }
        private int id { get; set; }
        private int id_venta { get; set; }

        private void Modificar_Click(object sender, EventArgs e)
        {
            if (dataGridDetalle.SelectedRows.Count > 0)
            {
                txtCantidad.Enabled = true;
                txtProducto.Enabled = true;
                txtPrecio.Enabled = true;
                Terminar.Enabled = true;
                Cancelar.Enabled = true;

                id = Convert.ToInt32(dataGridDetalle.SelectedRows[0].Cells["Id"].Value);
                id_venta = Convert.ToInt32(dataGridDetalle.SelectedRows[0].Cells["IdVenta"].Value);
                txtProducto.Text = dataGridDetalle.SelectedRows[0].Cells["CodigoProducto"].Value.ToString();
                txtCantidad.Text = dataGridDetalle.SelectedRows[0].Cells["Cantidad"].Value.ToString();
                txtPrecio.Text = dataGridDetalle.SelectedRows[0].Cells["Precio"].Value.ToString();

                cantidad_anterior = Convert.ToInt32(dataGridDetalle.SelectedRows[0].Cells["Cantidad"].Value);
                precio_anterior = Convert.ToSingle(dataGridDetalle.SelectedRows[0].Cells["Precio"].Value);

                bandera = true;
            }
        }

        private float total { get; set; }

        private void Siguiente_Click(object sender, EventArgs e)
        {
            var detalle = new DetalleVenta();
            dataGridVentas.Rows[dataGridVentas.Rows.Count - 1].Selected = true;
            var id = Convert.ToInt32(dataGridVentas.SelectedRows[0].Cells["Id"].Value);
            detalle.IdVenta = id;
            detalle.CodigoProducto = txtProducto.Text;
            detalle.Cantidad = Convert.ToInt32(txtCantidad.Text);
            detalle.Precio = Convert.ToSingle(txtPrecio.Text);
            var cantidad = Convert.ToInt32(txtCantidad.Text);
            total += (Convert.ToSingle(txtPrecio.Text) * cantidad);
            DetalleVenta.Agregar(detalle);

            txtCantidad.Clear();
            txtPrecio.Clear();
            txtProducto.Clear();
            dataGridDetalle.DataSource = DetalleVenta.Listar(id);
        }

        private void Terminar_Click(object sender, EventArgs e)
        {
            txtCantidad.Enabled = false;
            txtProducto.Enabled = false;
            txtPrecio.Enabled = false;
            Siguiente.Enabled = false;
            Terminar.Enabled = false;
            Cancelar.Enabled = false;
            Modificar.Enabled = true;

            if (bandera)
            {
                bandera = false;

                var detalle = new DetalleVenta();
                detalle.Id = id;
                detalle.IdVenta = id_venta;
                detalle.CodigoProducto = txtProducto.Text;
                detalle.Cantidad = Convert.ToInt32(txtCantidad.Text);
                detalle.Precio = Convert.ToSingle(txtPrecio.Text);

                dataGridVentas.Rows[id_venta - 1].Selected = true;
                total_anterior = Convert.ToSingle(dataGridVentas.SelectedRows[0].Cells["Total"].Value);
                
                total = total_anterior - (precio_anterior*cantidad_anterior) + (Convert.ToSingle(txtPrecio.Text) * Convert.ToInt32(txtCantidad.Text));
                DetalleVenta.Modificar(detalle);

                dataGridDetalle.DataSource = DetalleVenta.Listar(id);

                var venta = new Venta();
                venta.Id = id_venta;
                venta.Fecha = DateTime.Now;
                venta.Total = total;
                Venta.Modificar(venta);

                dataGridVentas.DataSource = Venta.Listar();
                dataGridDetalle.DataSource = DetalleVenta.Todos();
            }
            else
            {
                var venta = new Venta();
                dataGridVentas.Rows[dataGridVentas.Rows.Count - 1].Selected = true;
                venta.Id = Convert.ToInt32(dataGridVentas.SelectedRows[0].Cells["Id"].Value);
                venta.Fecha = DateTime.Now;
                venta.Total = total;
                Venta.Modificar(venta);

                dataGridVentas.DataSource = Venta.Listar();
                dataGridDetalle.DataSource = DetalleVenta.Todos();
            }
            total = 0;
        }

        private float total_anterior { get; set; }

        private void VerDetalle_Click(object sender, EventArgs e)
        {
            if (dataGridVentas.SelectedRows.Count > 0)
            {
                var id = Convert.ToInt32(dataGridVentas.SelectedRows[0].Cells["Id"].Value);
                dataGridDetalle.DataSource = DetalleVenta.Listar(id);
            }
        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void label4_Click(object sender, EventArgs e)
        {

        }

        private void agregarProductoToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var frm = new AgregarProducto();
            this.Hide();
            frm.Show();
        }

        private void verProductosToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var frm = new ListarProductos();
            this.Hide();
            frm.Show();
        }

        private void verStockToolStripMenuItem_Click(object sender, EventArgs e)
        {
        }

        private void agregarProveedorToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var frm = new AgregarProveedor();
            this.Hide();
            frm.Show();
        }

        private void mostrarProveedoresToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var frm = new ListarProveedores();
            this.Hide();
            frm.Show();
        }

        private void realizarPedidoToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var frm = new AgregarPedido();
            this.Hide();
            frm.Show();
        }

        private void verPedidosToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var frm = new ListarPedidos();
            this.Hide();
            frm.Show();
        }

        private void Cancelar_Click(object sender, EventArgs e)
        {
            txtCantidad.Clear();
            txtPrecio.Clear();
            txtProducto.Clear();
        }
    }
}
