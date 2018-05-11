namespace Sokoban
{
    partial class frm_tablero
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
            this.sokobanCtrl1 = new Sokoban.SokobanCtrl();
            this.SuspendLayout();
            // 
            // sokobanCtrl1
            // 
            this.sokobanCtrl1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.sokobanCtrl1.Juego = null;
            this.sokobanCtrl1.Location = new System.Drawing.Point(0, 0);
            this.sokobanCtrl1.Name = "sokobanCtrl1";
            this.sokobanCtrl1.Size = new System.Drawing.Size(406, 409);
            this.sokobanCtrl1.TabIndex = 0;
            // 
            // frm_tablero
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(406, 409);
            this.Controls.Add(this.sokobanCtrl1);
            this.KeyPreview = true;
            this.Name = "frm_tablero";
            this.Text = "frm_tablero";
            this.Load += new System.EventHandler(this.frm_tablero_Load);
            this.KeyUp += new System.Windows.Forms.KeyEventHandler(this.frm_tablero_KeyUp);
            this.ResumeLayout(false);

        }

        #endregion

        private SokobanCtrl sokobanCtrl1;

        

    }
}