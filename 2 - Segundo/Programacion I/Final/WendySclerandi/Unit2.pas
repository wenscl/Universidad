unit Unit2;

interface

uses
  Windows, Messages, SysUtils, Classes, Graphics, Controls, Forms, Dialogs,
  Db, DBTables, Grids, DBGrids, StdCtrls, Menus;

type
  TfrmEjercicio2 = class(TForm)
    DBGrid1: TDBGrid;
    DataSourcePropietarios: TDataSource;
    DataSourcePropiedades: TDataSource;
    DBGrid2: TDBGrid;
    tblPropietarios: TTable;
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
    tblPropietariosIDPropietario: TIntegerField;
    tblPropietariosNombre: TStringField;
    tblPropietariosTelefono: TStringField;
    tblPropietariosDomicilio: TStringField;
    MainMenu1: TMainMenu;
    Ejercicio11: TMenuItem;
    Ejercicio21: TMenuItem;
    Ejercicio31: TMenuItem;
    GroupBox1: TGroupBox;
    Label1: TLabel;
    edtPropietario: TEdit;
    Buscar: TButton;
    procedure FormCreate(Sender: TObject);
    procedure BuscarClick(Sender: TObject);
    procedure Ejercicio11Click(Sender: TObject);
    procedure Ejercicio31Click(Sender: TObject);
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  frmEjercicio2: TfrmEjercicio2;

implementation

uses Unit1, Unit3;

{$R *.DFM}

procedure TfrmEjercicio2.FormCreate(Sender: TObject);
begin
        tblPropietarios.open;
        tblPropiedades.open;
end;

procedure TfrmEjercicio2.BuscarClick(Sender: TObject);
begin
        tblPropietarios.FindKey([edtPropietario.text]);
end;

procedure TfrmEjercicio2.Ejercicio11Click(Sender: TObject);
begin
        frmEjercicio1.show;
end;

procedure TfrmEjercicio2.Ejercicio31Click(Sender: TObject);
begin
        frmEjercicio3.show;
end;

end.
