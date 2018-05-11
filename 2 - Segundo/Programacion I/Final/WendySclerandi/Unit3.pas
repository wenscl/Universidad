unit Unit3;

interface

uses
  Windows, Messages, SysUtils, Classes, Graphics, Controls, Forms, Dialogs,
  Db, DBTables, StdCtrls, Grids, DBGrids, Menus;

type
        TRPropietario = record
                                IDPropiedad, IDLocalidad, Destino: integer;
                                Domicilio: string [50];
                        End;
        TPropietario = File of TRPropietario;

  TfrmEjercicio3 = class(TForm)
    tblPropiedades: TTable;
    tblPropietarios: TTable;
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
    DBGrid1: TDBGrid;
    DataSource1: TDataSource;
    MainMenu1: TMainMenu;
    Ejercicio11: TMenuItem;
    Ejercicio21: TMenuItem;
    Ejercicio31: TMenuItem;
    GroupBox1: TGroupBox;
    edtDestino2: TEdit;
    edtPrecioDesde: TEdit;
    edtPrecioHasta: TEdit;
    Calcular: TButton;
    edtCantidadProp: TEdit;
    Label3: TLabel;
    Label4: TLabel;
    Label5: TLabel;
    Label6: TLabel;
    GroupBox2: TGroupBox;
    edtIDPropietario: TEdit;
    GenerarArchivo: TButton;
    Label7: TLabel;
    GroupBox3: TGroupBox;
    Destino: TRadioButton;
    Estado: TRadioButton;
    CantidadDormitoris: TRadioButton;
    edtValor: TEdit;
    Filtrar: TButton;
    Cancelar: TButton;
    edtCantidad: TEdit;
    Label2: TLabel;
    Label1: TLabel;
    procedure FiltrarClick(Sender: TObject);
    procedure FormCreate(Sender: TObject);
    procedure GenerarArchivoClick(Sender: TObject);
    procedure CancelarClick(Sender: TObject);
    procedure CalcularClick(Sender: TObject);
    procedure Ejercicio11Click(Sender: TObject);
    procedure Ejercicio21Click(Sender: TObject);
  private
    { Private declarations }
    function fncFiltroPropiedades(Tipo: integer; Valor: string): integer;
    procedure prcGenerarArchivo(IDPropietario: string);
    function fncCantidadPropiedades(Destino, PrecioDesde, PrecioHasta: string): integer;
  public
    { Public declarations }
  end;

var
  frmEjercicio3: TfrmEjercicio3;
  Tipo: integer;
  Valor: string;
  Propietario: TPropietario;
  VPropietario: TRPropietario;

implementation

uses Unit1, Unit2;

{$R *.DFM}


{ TfrmEjercicio3 }

function TfrmEjercicio3.fncFiltroPropiedades(Tipo: integer; Valor: string): integer;
var c: integer;
begin
        c:= 0;
        If Tipo = 1 then
                tblPropiedades.filter:= 'Destino=' + QuotedStr(Valor)
        Else
                If Tipo = 2 then
                        tblPropiedades.filter:= 'Estado=' + QuotedStr(Valor)
                Else
                        tblPropiedades.filter:= 'CantidadDormitorios=' + QuotedStr(Valor);
        tblPropiedades.filtered:= True;
        While not tblPropiedades.eof do
        Begin
                c:= c + 1;
                tblPropiedades.next;
        End;
        tblPropiedades.first;
        fncFiltroPropiedades:= c;
end;

procedure TfrmEjercicio3.FiltrarClick(Sender: TObject);
begin
        If Destino.checked then
                Tipo:= 1
        Else
                If Estado.checked then
                        Tipo:= 2
                Else
                        Tipo:= 3;
        edtCantidad.text:= IntToStr(fncFiltroPropiedades(Tipo, edtValor.text));
end;

procedure TfrmEjercicio3.FormCreate(Sender: TObject);
begin
        tblPropiedades.open;
        tblPropietarios.open;
        AssignFile(Propietario, 'D:\WendySclerandi\ArchivoPropietarios.dat');
        Rewrite(Propietario);
end;

procedure TfrmEjercicio3.GenerarArchivoClick(Sender: TObject);
begin
        prcGenerarArchivo(edtIDPropietario.text);
end;

procedure TfrmEjercicio3.prcGenerarArchivo(IDPropietario: string);
begin
        tblPropiedades.filter:= 'IDPropietario=' + QuotedStr(IDPropietario);
        tblPropiedades.filtered:= True;
        Reset(Propietario);
        While not tblPropiedades.eof do
        Begin
                VPropietario.IDPropiedad:= tblPropiedadesIDPropiedad.value;
                VPropietario.Domicilio:= tblPropiedadesDomicilio.value;
                VPropietario.IDLocalidad:= tblPropiedadesIDLocalidad.value;
                VPropietario.Destino:= tblPropiedadesDestino.value;
                Write(Propietario, VPropietario);
                tblPropiedades.next;
        End;
        tblPropiedades.filtered:= False;
        CloseFile(Propietario);
end;

function TfrmEjercicio3.fncCantidadPropiedades(Destino, PrecioDesde,
  PrecioHasta: string): integer;
var cant: integer;
begin
        cant:= 0;
        tblPropiedades.IndexName:= 'PorPrecio';
        tblPropiedades.SetRange([PrecioDesde],[PrecioHasta]);
        tblPropiedades.filter:= 'Destino=' + QuotedStr(Destino);
        tblPropiedades.filtered:= True;
        While not tblPropiedades.eof do
        Begin
                cant:= cant + 1;
                tblPropiedades.next;
        End;
        tblPropiedades.filtered:= False;
        tblPropiedades.CancelRange();
        fncCantidadPropiedades:= cant;
end;

procedure TfrmEjercicio3.CancelarClick(Sender: TObject);
begin
        tblPropiedades.filtered:= False;
end;

procedure TfrmEjercicio3.CalcularClick(Sender: TObject);
begin
        edtCantidadProp.text:= IntToStr(fncCantidadPropiedades(edtDestino2.text, edtPrecioDesde.text, edtPrecioHasta.text));
end;

procedure TfrmEjercicio3.Ejercicio11Click(Sender: TObject);
begin
        frmEjercicio1.show;
end;

procedure TfrmEjercicio3.Ejercicio21Click(Sender: TObject);
begin
        frmEjercicio2.show;
end;

end.
