﻿namespace Prototipo.Forms
{
    partial class AgregarProveedor
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(AgregarProveedor));
            this.Nombre = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.txtNombre = new System.Windows.Forms.TextBox();
            this.txtDireccion = new System.Windows.Forms.TextBox();
            this.txtTelefono = new System.Windows.Forms.TextBox();
            this.txtMail = new System.Windows.Forms.TextBox();
            this.panel1 = new System.Windows.Forms.Panel();
            this.txtCiudad = new System.Windows.Forms.TextBox();
            this.label5 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.Cancelar = new System.Windows.Forms.Button();
            this.Guardar = new System.Windows.Forms.Button();
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.ventasToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.agregarVentaToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.productosToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.agregarProductoToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.verProductosToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.verStockToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.proveedoresToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.agregarProveedorToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.mostrarProveedoresToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.realizarPedidoToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.verPedidosToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.reportesToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.mostrarReportesToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.panel1.SuspendLayout();
            this.menuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // Nombre
            // 
            this.Nombre.AutoSize = true;
            this.Nombre.Location = new System.Drawing.Point(21, 20);
            this.Nombre.Name = "Nombre";
            this.Nombre.Size = new System.Drawing.Size(64, 19);
            this.Nombre.TabIndex = 0;
            this.Nombre.Text = "Nombre";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(21, 104);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(74, 19);
            this.label2.TabIndex = 1;
            this.label2.Text = "Dirección";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(21, 145);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(66, 19);
            this.label3.TabIndex = 2;
            this.label3.Text = "Teléfono";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(21, 189);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(38, 19);
            this.label4.TabIndex = 3;
            this.label4.Text = "Mail";
            // 
            // txtNombre
            // 
            this.txtNombre.Location = new System.Drawing.Point(134, 17);
            this.txtNombre.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.txtNombre.Name = "txtNombre";
            this.txtNombre.Size = new System.Drawing.Size(244, 24);
            this.txtNombre.TabIndex = 1;
            // 
            // txtDireccion
            // 
            this.txtDireccion.Location = new System.Drawing.Point(134, 101);
            this.txtDireccion.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.txtDireccion.Name = "txtDireccion";
            this.txtDireccion.Size = new System.Drawing.Size(244, 24);
            this.txtDireccion.TabIndex = 3;
            // 
            // txtTelefono
            // 
            this.txtTelefono.Location = new System.Drawing.Point(134, 142);
            this.txtTelefono.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.txtTelefono.Name = "txtTelefono";
            this.txtTelefono.Size = new System.Drawing.Size(244, 24);
            this.txtTelefono.TabIndex = 4;
            // 
            // txtMail
            // 
            this.txtMail.Location = new System.Drawing.Point(134, 185);
            this.txtMail.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.txtMail.Name = "txtMail";
            this.txtMail.Size = new System.Drawing.Size(244, 24);
            this.txtMail.TabIndex = 5;
            // 
            // panel1
            // 
            this.panel1.BackColor = System.Drawing.Color.GhostWhite;
            this.panel1.Controls.Add(this.txtCiudad);
            this.panel1.Controls.Add(this.label5);
            this.panel1.Controls.Add(this.Nombre);
            this.panel1.Controls.Add(this.txtMail);
            this.panel1.Controls.Add(this.label2);
            this.panel1.Controls.Add(this.txtTelefono);
            this.panel1.Controls.Add(this.label3);
            this.panel1.Controls.Add(this.txtDireccion);
            this.panel1.Controls.Add(this.label4);
            this.panel1.Controls.Add(this.txtNombre);
            this.panel1.Font = new System.Drawing.Font("Century Gothic", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.panel1.Location = new System.Drawing.Point(396, 143);
            this.panel1.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(396, 229);
            this.panel1.TabIndex = 8;
            // 
            // txtCiudad
            // 
            this.txtCiudad.Location = new System.Drawing.Point(134, 59);
            this.txtCiudad.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.txtCiudad.Name = "txtCiudad";
            this.txtCiudad.Size = new System.Drawing.Size(244, 24);
            this.txtCiudad.TabIndex = 2;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(21, 63);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(62, 19);
            this.label5.TabIndex = 8;
            this.label5.Text = "Ciudad";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.BackColor = System.Drawing.Color.Transparent;
            this.label1.Font = new System.Drawing.Font("Century Gothic", 14F, System.Drawing.FontStyle.Underline, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(479, 101);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(221, 22);
            this.label1.TabIndex = 9;
            this.label1.Text = "Carga de Proveedores";
            // 
            // Cancelar
            // 
            this.Cancelar.BackColor = System.Drawing.Color.GhostWhite;
            this.Cancelar.FlatAppearance.BorderSize = 2;
            this.Cancelar.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.Cancelar.Font = new System.Drawing.Font("Century Gothic", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Cancelar.Image = ((System.Drawing.Image)(resources.GetObject("Cancelar.Image")));
            this.Cancelar.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.Cancelar.Location = new System.Drawing.Point(483, 405);
            this.Cancelar.Name = "Cancelar";
            this.Cancelar.Size = new System.Drawing.Size(110, 46);
            this.Cancelar.TabIndex = 7;
            this.Cancelar.Text = "Cancelar";
            this.Cancelar.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.Cancelar.UseVisualStyleBackColor = false;
            this.Cancelar.Click += new System.EventHandler(this.Cancelar_Click);
            // 
            // Guardar
            // 
            this.Guardar.BackColor = System.Drawing.Color.GhostWhite;
            this.Guardar.FlatAppearance.BorderSize = 2;
            this.Guardar.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.Guardar.Font = new System.Drawing.Font("Century Gothic", 10F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Guardar.Image = ((System.Drawing.Image)(resources.GetObject("Guardar.Image")));
            this.Guardar.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.Guardar.Location = new System.Drawing.Point(599, 405);
            this.Guardar.Name = "Guardar";
            this.Guardar.Size = new System.Drawing.Size(110, 46);
            this.Guardar.TabIndex = 6;
            this.Guardar.Text = "Guardar";
            this.Guardar.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.Guardar.UseVisualStyleBackColor = false;
            this.Guardar.Click += new System.EventHandler(this.Agregar_Click);
            // 
            // menuStrip1
            // 
            this.menuStrip1.BackColor = System.Drawing.Color.GhostWhite;
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.ventasToolStripMenuItem,
            this.productosToolStripMenuItem,
            this.proveedoresToolStripMenuItem,
            this.reportesToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(1180, 24);
            this.menuStrip1.TabIndex = 15;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // ventasToolStripMenuItem
            // 
            this.ventasToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.agregarVentaToolStripMenuItem});
            this.ventasToolStripMenuItem.Name = "ventasToolStripMenuItem";
            this.ventasToolStripMenuItem.Size = new System.Drawing.Size(53, 20);
            this.ventasToolStripMenuItem.Text = "Ventas";
            // 
            // agregarVentaToolStripMenuItem
            // 
            this.agregarVentaToolStripMenuItem.Name = "agregarVentaToolStripMenuItem";
            this.agregarVentaToolStripMenuItem.Size = new System.Drawing.Size(148, 22);
            this.agregarVentaToolStripMenuItem.Text = "Agregar venta";
            this.agregarVentaToolStripMenuItem.Click += new System.EventHandler(this.agregarVentaToolStripMenuItem_Click);
            // 
            // productosToolStripMenuItem
            // 
            this.productosToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.agregarProductoToolStripMenuItem,
            this.verProductosToolStripMenuItem,
            this.verStockToolStripMenuItem});
            this.productosToolStripMenuItem.Name = "productosToolStripMenuItem";
            this.productosToolStripMenuItem.Size = new System.Drawing.Size(73, 20);
            this.productosToolStripMenuItem.Text = "Productos";
            // 
            // agregarProductoToolStripMenuItem
            // 
            this.agregarProductoToolStripMenuItem.Name = "agregarProductoToolStripMenuItem";
            this.agregarProductoToolStripMenuItem.Size = new System.Drawing.Size(168, 22);
            this.agregarProductoToolStripMenuItem.Text = "Agregar producto";
            this.agregarProductoToolStripMenuItem.Click += new System.EventHandler(this.agregarProductoToolStripMenuItem_Click);
            // 
            // verProductosToolStripMenuItem
            // 
            this.verProductosToolStripMenuItem.Name = "verProductosToolStripMenuItem";
            this.verProductosToolStripMenuItem.Size = new System.Drawing.Size(168, 22);
            this.verProductosToolStripMenuItem.Text = "Ver productos";
            this.verProductosToolStripMenuItem.Click += new System.EventHandler(this.verProductosToolStripMenuItem_Click);
            // 
            // verStockToolStripMenuItem
            // 
            this.verStockToolStripMenuItem.Name = "verStockToolStripMenuItem";
            this.verStockToolStripMenuItem.Size = new System.Drawing.Size(168, 22);
            this.verStockToolStripMenuItem.Text = "Ver stock";
            // 
            // proveedoresToolStripMenuItem
            // 
            this.proveedoresToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.agregarProveedorToolStripMenuItem,
            this.mostrarProveedoresToolStripMenuItem,
            this.realizarPedidoToolStripMenuItem,
            this.verPedidosToolStripMenuItem});
            this.proveedoresToolStripMenuItem.Name = "proveedoresToolStripMenuItem";
            this.proveedoresToolStripMenuItem.Size = new System.Drawing.Size(84, 20);
            this.proveedoresToolStripMenuItem.Text = "Proveedores";
            // 
            // agregarProveedorToolStripMenuItem
            // 
            this.agregarProveedorToolStripMenuItem.Name = "agregarProveedorToolStripMenuItem";
            this.agregarProveedorToolStripMenuItem.Size = new System.Drawing.Size(173, 22);
            this.agregarProveedorToolStripMenuItem.Text = "Agregar proveedor";
            // 
            // mostrarProveedoresToolStripMenuItem
            // 
            this.mostrarProveedoresToolStripMenuItem.Name = "mostrarProveedoresToolStripMenuItem";
            this.mostrarProveedoresToolStripMenuItem.Size = new System.Drawing.Size(173, 22);
            this.mostrarProveedoresToolStripMenuItem.Text = "Ver proveedores";
            this.mostrarProveedoresToolStripMenuItem.Click += new System.EventHandler(this.mostrarProveedoresToolStripMenuItem_Click);
            // 
            // realizarPedidoToolStripMenuItem
            // 
            this.realizarPedidoToolStripMenuItem.Name = "realizarPedidoToolStripMenuItem";
            this.realizarPedidoToolStripMenuItem.Size = new System.Drawing.Size(173, 22);
            this.realizarPedidoToolStripMenuItem.Text = "Realizar pedido";
            this.realizarPedidoToolStripMenuItem.Click += new System.EventHandler(this.realizarPedidoToolStripMenuItem_Click);
            // 
            // verPedidosToolStripMenuItem
            // 
            this.verPedidosToolStripMenuItem.Name = "verPedidosToolStripMenuItem";
            this.verPedidosToolStripMenuItem.Size = new System.Drawing.Size(173, 22);
            this.verPedidosToolStripMenuItem.Text = "Ver pedidos";
            this.verPedidosToolStripMenuItem.Click += new System.EventHandler(this.verPedidosToolStripMenuItem_Click);
            // 
            // reportesToolStripMenuItem
            // 
            this.reportesToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.mostrarReportesToolStripMenuItem});
            this.reportesToolStripMenuItem.Name = "reportesToolStripMenuItem";
            this.reportesToolStripMenuItem.Size = new System.Drawing.Size(65, 20);
            this.reportesToolStripMenuItem.Text = "Reportes";
            // 
            // mostrarReportesToolStripMenuItem
            // 
            this.mostrarReportesToolStripMenuItem.Name = "mostrarReportesToolStripMenuItem";
            this.mostrarReportesToolStripMenuItem.Size = new System.Drawing.Size(161, 22);
            this.mostrarReportesToolStripMenuItem.Text = "Mostrar reportes";
            // 
            // AgregarProveedor
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("$this.BackgroundImage")));
            this.ClientSize = new System.Drawing.Size(1180, 557);
            this.Controls.Add(this.menuStrip1);
            this.Controls.Add(this.Cancelar);
            this.Controls.Add(this.Guardar);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.panel1);
            this.Font = new System.Drawing.Font("Century Gothic", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.Fixed3D;
            this.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.Name = "AgregarProveedor";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Carga de Proveedores";
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label Nombre;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.TextBox txtNombre;
        private System.Windows.Forms.TextBox txtDireccion;
        private System.Windows.Forms.TextBox txtTelefono;
        private System.Windows.Forms.TextBox txtMail;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button Cancelar;
        private System.Windows.Forms.Button Guardar;
        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem ventasToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem agregarVentaToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem productosToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem agregarProductoToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem verProductosToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem verStockToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem proveedoresToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem agregarProveedorToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem mostrarProveedoresToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem realizarPedidoToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem reportesToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem mostrarReportesToolStripMenuItem;
        private System.Windows.Forms.TextBox txtCiudad;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.ToolStripMenuItem verPedidosToolStripMenuItem;
    }
}