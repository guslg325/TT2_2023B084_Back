from handlers.getHistorialExistencias import get_historial_existencias_handler
from handlers.utils import to_mx_timezone
import pytest
from handlers.hacerCompraHandler import hacer_compra_handler;
from handlers.getVentasListHandler import get_ventas_handler;
from handlers.getAllMarcasHandler import get_all_marcas_handler;
from handlers.addProductoHandler import add_producto_handler;
from handlers.addStockHandler import add_stock_handler;
from handlers.removeStockHandler import remove_stock_handler;
from handlers.desactivarProductoHandler import desactivar_producto_handler;
from handlers.getMermasHandler import get_mermas_handler;
from handlers.getExistenciasHandler import get_existencias_handler;
import pprint
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

def sum(a, b):
  return a + b;
# declare type Producto = {
#   key: string;
#   codigo: string;
#   nombre: string;
#   marca: string;
#   stock: number;
#   precio: number;
# };
# declare type VentaItem = {
#   key: string;
#   cantidad: number;
#   producto: Producto;
# }
# declare type Venta = {
#   id: number;
#   fecha: string;
#   items: VentaItem[];
#   cantidad: number;
#   total: number;
# }

def test_hacer_compra():
  lista = [
    {
      "key": "PROD003",
      "cantidad": 2,
      "producto": {
        "key": "PROD003",
        "codigo": "PROD001",
        "nombre": "Producto 1",
        "marca": "Marca 1",
        "stock": 10,
        "precio": 100
      }
    },
    {
      "key": "PROD004",
      "cantidad": 2,
      "producto": {
        "key": "PROD004",
        "codigo": "PROD001",
        "nombre": "Producto 1",
        "marca": "Marca 1",
        "stock": 10,
        "precio": 100
      }
    }
  ]
  #hacer_compra_handler(lista)
  # producto = {
  #     "key": "1234",
  #     "codigo": "123",
  #     "nombre": "producto por añadir 3",
  #     "marca": 1,
  #     "stock": 123,
  #     "precio": 500.05
  # }
  # add_producto_handler(producto)
  # remove_stock_handler({
  #   "codigo": "PROD001",
  #   "merma": 100,
  # })

  # print(get_ventas_handler())
  ##desactivar_producto_handler("PROD001");
  dat = get_ventas_handler()
  print(
    list(map(lambda x: x['fecha'],dat))
  )
  # fecha = "2023-10-24 21:42:00"
  # dt = datetime.fromisoformat(fecha)
  # dt = dt.replace(tzinfo=timezone.utc)
  # fecha = dat[1]["fecha"]
  # dtmex = to_mx_timezone(fecha)
  # mxtimezone = ZoneInfo("America/Mexico_City")
  # dtmex = fecha.astimezone(mxtimezone)
  # print(fecha)
  # print(dtmex)
  assert True

test_hacer_compra()