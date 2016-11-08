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
    public partial class ListarProveedores : Form
    {
        public ListarProveedores()
        {
            InitializeComponent();
        }

        private void Buscar_Click(object sender, EventArgs e)
        {
            dataGridView1.DataSource = Proveedor.Buscar(txtBuscar.Text).ToList();
        }

        private void Limpiar_Click(object sender, EventArgs e)
        {
            dataGridView1.DataSource = Proveedor.Listar();
        }

        private void ListarProveedores_Load(object sender, EventArgs e)
        {
            dataGridView1.DataSource = Proveedor.Listar();
        }

        private void Agregar_Click(object sender, EventArgs e)
        {
            var frm = new AgregarProveedor();
            this.Hide();
            frm.Show();
        }

        private void Modificar_Click(object sender, EventArgs e)
        {
            if (dataGridView1.SelectedRows.Count > 0)
            {
                var id = Convert.ToInt32(dataGridView1.SelectedRows[0].Cells["Id"].Value);
                var nombre = dataGridView1.SelectedRows[0].Cells["Nombre"].Value.ToString();
                var ciudad = dataGridView1.SelectedRows[0].Cells["Ciudad"].Value.ToString();
                var direccion = dataGridView1.SelectedRows[0].Cells["Direccion"].Value.ToString();
                var telefono = dataGridView1.SelectedRows[0].Cells["Telefono"].Value.ToString();
                var mail = dataGridView1.SelectedRows[0].Cells["Mail"].Value.ToString();

                var frm = new ModificarProveedor(id, nombre, ciudad, direccion, telefono, mail);
                this.Hide();
                frm.Show();
            }
        }

        private void Eliminar_Click(object sender, EventArgs e)
        {
            var id = dataGridView1.SelectedRows[0].Cells["Id"].Value.ToString();
            Proveedor.Eliminar(Convert.ToInt32(id));
            dataGridView1.DataSource = Proveedor.Listar();
        }

        private void agregarVentaToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var frm = new AgregarVenta();
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

        private void agregarProveedorToolStripMenuItem_Click(object sender, EventArgs e)
        {
            var frm = new AgregarProveedor();
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
    }
}
