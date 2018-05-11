unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Classes, Graphics, Controls, Forms, Dialogs,
  ExtCtrls, DBCtrls, Grids, DBGrids, StdCtrls, Db, Mask, DBTables, Menus;

type
  TfrmEjercicio1 = class(TForm)
    tblPropietarios: TTable;
    tblLocalidades: TTable;
    tblPropietariosIDPropietario: TIntegerField;
    tblPropietariosNombre: TStringField;
    tblPropietariosTelefono: TStringField;
    tblPropietariosDomicilio: TStringField;
    tblLocalidadesIDLocalidad: TIntegerField;
    tblLocalidadesNombreLocalidad: TStringField;
    DBGrid1: TDBGrid;
    DBNavigator1: TDBNavigator;
    tblPropiedades: TTable;
    tblPropiedadesIDPropietario: TIntegerField;
    tblPropiedadesIDPropiedad: TIntegerField;
    tblPropiedadesIDLocalidad: TIntegerField;
    tblPropiedadesDestino: TIntegerField;
    tblPropiedadesCantidadDormitorios: TIntegerField;
    tblPropiedadesGaraje: TBooleanField;
    tblPropiedadesPatio: TBooleanField;
    tblPropiedadesMetrosCubiertos: TFloatField;
    tblPropiedadesPrecioVenta: TCurrencyField;
    tblPropiedadesDomicilio: TStringField;
    tblPropiedadesEstado: TIntegerField;
    tblPropiedadesNombreLocalidad: TStringField;
    tblPropiedadesNombrePropietario: TStringField;
    tblPropiedadesDescripcionDestino: TStringField;
    tblPropiedadesDescripcionEstado: TStringField;
    Label1: TLabel;
    DBEdit1: TDBEdit;
    DataSource1: TDataSource;
    Label2: TLabel;
    DBEdit2: TDBEdit;
    Label3: TLabel;
    DBEdit3: TDBEdit;
    Label4: TLabel;
    DBEdit4: TDBEdit;
    Label5: TLabel;
    DBEdit5: TDBEdit;
    DBCheckBox1: TDBCheckBox;
    DBCheckBox2: TDBCheckBox;
    Label6: TLabel;
    DBEdit6: TDBEdit;
    Label7: TLabel;
    DBEdit7: TDBEdit;
    Label8: TLabel;
    DBEdit8: TDBEdit;
    Label9: TLabel;
    DBEdit9: TDBEdit;
    Label10: TLabel;
    DBLookupComboBox1: TDBLookupComboBox;
    Label11: TLabel;
    DBLookupComboBox2: TDBLookupComboBox;
    Label12: TLabel;
    edtDestino: TDBEdit;
    Label13: TLabel;
    edtEstado: TDBEdit;
    MainMenu1: TMainMenu;
    Ejercicio11: TMenuItem;
    Ejercicio21: TMenuItem;
    Ejercicio31: TMenuItem;
    procedure FormCreate(Sender: TObject);
    procedure tblPropiedadesAfterInsert(DataSet: TDataSet);
    procedure tblPropiedadesBeforeInsert(DataSet: TDataSet);
    procedure tblPropiedadesBeforeDelete(DataSet: TDataSet);
    procedure tblPropiedadesBeforePost(DataSet: TDataSet);
    procedure tblPropiedadesCalcFields(DataSet: TDataSet);
    procedure Ejercicio21Click(Sender: TObject);
    procedure Ejercicio31Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  frmEjercicio1: TfrmEjercicio1;
  IDPropiedad: integer;

implementation

uses Unit2, Unit3;

{$R *.DFM}

procedure TfrmEjercicio1.FormCreate(Sender: TObject);
begin
        tblPropiedades.open;
        tblPropietarios.open;
        tblLocalidades.open;
end;

procedure TfrmEjercicio1.tblPropiedadesAfterInsert(DataSet: TDataSet);
begin
        tblPropiedadesIDPropiedad.value:= IDPropiedad;
        tblPropiedadesEstado.value:= 1;
        tblPropiedadesGaraje.value:= False;
        tblPropiedadesPatio.value:= False;
end;

procedure TfrmEjercicio1.tblPropiedadesBeforeInsert(DataSet: TDataSet);
begin
        tblPropiedades.last;
        IDPropiedad:= tblPropiedadesIDPropiedad.value + 1;
end;

procedure TfrmEjercicio1.tblPropiedadesBeforeDelete(DataSet: TDataSet);
begin
        If Application.MessageBox('Seguro que desea eliminar?', 'Atencion', MB_YESNO) = IDNO then
                Abort;
end;

procedure TfrmEjercicio1.tblPropiedadesBeforePost(DataSet: TDataSet);
begin
        If tblPropiedadesDomicilio.isnull or tblPropiedadesIDLocalidad.isnull or tblPropiedadesDestino.isnull
        or tblPropiedadesCantidadDormitorios.isnull or tblPropiedadesMetrosCubiertos.isnull or
        tblPropiedadesPrecioVenta.isnull or tblPropiedadesIDPropietario.isnull then
        Begin
                Application.MessageBox('Complete todos los campos', 'Atencion', MB_OK);
                Abort;
        End;
end;

procedure TfrmEjercicio1.tblPropiedadesCalcFields(DataSet: TDataSet);
begin
        If tblPropiedadesDestino.value = 1 then
                edtDestino.text:= 'Alquiler'
        Else
                edtDestino.text:= 'Venta';
        If tblPropiedadesEstado.value = 1 then
                edtEstado.text:= 'Disponible par alquiler'
        Else
                If tblPropiedadesEstado.value = 2 then
                        edtEstado.text:= 'En refaccion'
                Else
                        edtEstado.text:= 'Alquilada/Vendida';
end;

procedure TfrmEjercicio1.Ejercicio21Click(Sender: TObject);
begin
        frmEjercicio2.show;
end;

procedure TfrmEjercicio1.Ejercicio31Click(Sender: TObject);
begin
        frmEjercicio3.show
end;

end.
