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
    public partial class AgregarPedido : Form
    {
        public AgregarPedido()
        {
            InitializeComponent();
        }

        private void agregarProveedorToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var frm = new AgregarProveedor();
            this.Hide();
            frm.Show();
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

        private void mostrarProveedoresToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var frm = new ListarProveedores();
            this.Hide();
            frm.Show();
        }

        private void agregarVentaToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var frm = new AgregarVenta();
            this.Hide();
            frm.Show();
        }

        private bool bandera { get; set; }
        private int id_pedido { get; set; }

        private void Agregar_Click(object sender, EventArgs e)
        {
            if (bandera)
            {
                var pedido = new Pedido();
                pedido.Proveedor = comboBoxProveedor.Text;
                pedido.Fecha = dateTimePicker.Value;
                Pedido.Agregar(pedido);
                bandera = false;
                comboBoxProveedor.Enabled = false;
                dateTimePicker.Enabled = false;
                id_pedido = Convert.ToInt32(Pedido.Listar().Last().Id);
            }
            
            var detallePedido = new DetallePedido();
            detallePedido.IdPedido = id_pedido;
            detallePedido.Producto = comboBoxProducto.Text;
            detallePedido.Cantidad = Convert.ToInt32(txtCantidad.Text);
            DetallePedido.Agregar(detallePedido);

            txtCantidad.Clear();
            dataGridView1.DataSource = DetallePedido.Listar(id_pedido);
        }

        private void AgregarPedido_Load(object sender, EventArgs e)
        {
            txtCantidad.Clear();
            comboBoxProveedor.DataSource = Proveedor.Listar2();
            comboBoxProducto.DataSource = Producto.Listar2();
            bandera = true;
        }

        private void Enviar_Click(object sender, EventArgs e)
        {
            comboBoxProveedor.Enabled = true;
            dateTimePicker.Enabled = true;

            var frm = new ListarPedidos();
            this.Hide();
            frm.Show();
        }

        private void panel1_Paint(object sender, PaintEventArgs e)
        {

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
        }
    }
}
