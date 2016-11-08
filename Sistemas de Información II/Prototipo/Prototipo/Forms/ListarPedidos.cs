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
    public partial class ListarPedidos : Form
    {
        public ListarPedidos()
        {
            InitializeComponent();
        }

        private void ListarPedidos_Load(object sender, EventArgs e)
        {
            dataGridPedidos.DataSource = Pedido.Listar();
            dataGridDetalle.DataSource = DetallePedido.Todos();
        }

        private void Siguiente_Click(object sender, EventArgs e)
        {

        }

        private void Agregar_Click(object sender, EventArgs e)
        {
            var frm = new AgregarPedido();
            this.Hide();
            frm.Show();
        }

        private void Eliminar_Click(object sender, EventArgs e)
        {
            if (dataGridPedidos.SelectedRows.Count > 0)
            {
                var id = Convert.ToInt32(dataGridPedidos.SelectedRows[0].Cells["Id"].Value);
                var lista = DetallePedido.Listar(id);
                foreach (DetallePedido item in lista)
                {
                    DetallePedido.Eliminar(item.Id);
                }
                Pedido.Eliminar(id);
                dataGridPedidos.DataSource = Pedido.Listar();
                dataGridDetalle.DataSource = DetallePedido.Todos();
            }
        }

        private string proveedor { get; set; }
        private int id_pedido { get; set; }
        private DateTime fecha { get; set; }

        private void VerDetalle_Click(object sender, EventArgs e)
        {
            if (dataGridPedidos.SelectedRows.Count > 0)
            {
                proveedor = dataGridPedidos.SelectedRows[0].Cells["Proveedor"].Value.ToString();
                id_pedido = Convert.ToInt32(dataGridPedidos.SelectedRows[0].Cells["Id"].Value);
                fecha = Convert.ToDateTime(dataGridPedidos.SelectedRows[0].Cells["Fecha"].Value);
                dataGridDetalle.DataSource = DetallePedido.Listar(id_pedido);
            }
        }

        private int id { get; set; }

        private void Modificar_Click(object sender, EventArgs e)
        {
            if (dataGridDetalle.SelectedRows.Count > 0)
            {
                txtCantidad.Enabled = true;
                txtProducto.Enabled = true;
                Guardar.Enabled = true;
                Cancelar.Enabled = true;

                id = Convert.ToInt32(dataGridDetalle.SelectedRows[0].Cells["Id"].Value);
                txtProducto.Text = dataGridDetalle.SelectedRows[0].Cells["Producto"].Value.ToString();
                txtCantidad.Text = dataGridDetalle.SelectedRows[0].Cells["Cantidad"].Value.ToString();
            }
        }

        private void Guardar_Click(object sender, EventArgs e)
        {
            txtCantidad.Enabled = false;
            txtProducto.Enabled = false;
            Guardar.Enabled = false;
            
            var detalle = new DetallePedido();
            detalle.Id = id;
            detalle.IdPedido = id_pedido;
            detalle.Producto = txtProducto.Text;
            detalle.Cantidad = Convert.ToInt32(txtCantidad.Text);
            
            DetallePedido.Modificar(detalle);

            dataGridDetalle.DataSource = DetallePedido.Listar(id);

            var pedido = new Pedido();
            pedido.Id = id_pedido;
            pedido.Proveedor = proveedor;
            pedido.Fecha = fecha;
            Pedido.Modificar(pedido);

            dataGridPedidos.DataSource = Pedido.Listar();
            dataGridDetalle.DataSource = DetallePedido.Todos();

            txtCantidad.Clear();
            txtProducto.Clear();
        }

        private void verPedidosToolStripMenuItem_Click(object sender, EventArgs e)
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

        private void agregarVentaToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var frm = new AgregarVenta();
            this.Hide();
            frm.Show();
        }

        private void Cancelar_Click(object sender, EventArgs e)
        {
            txtCantidad.Clear();
            txtProducto.Clear();

            txtProducto.Enabled = false;
            txtCantidad.Enabled = false;
            Cancelar.Enabled = false;
        }
    }
}
