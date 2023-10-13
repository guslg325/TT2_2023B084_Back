
import azure.functions as func
from sqlalchemy import select, insert, update
from .models import Venta, RegistroExistencia, RegistroMerma, Producto, DetalleVenta
from sqlalchemy.ext.serializer import loads, dumps
from functools import reduce
import json
from .connect import create_session
# SELECT * FROM DETALLE_VENTA dv;
# SELECT id_venta, SUM(cantidad) AS total_cantidad, SUM(subtotal) AS total FROM DETALLE_VENTA GROUP BY id_venta;

# SELECT
#     v.*,
#     dv.total_cantidad,
#     dv.total
# FROM
#     VENTA v
# LEFT JOIN
#     (SELECT id_venta, SUM(cantidad) AS total_cantidad, SUM(subtotal) AS total FROM DETALLE_VENTA GROUP BY id_venta) dv
# ON
#     v.id  = dv.id_venta;


# SELECT
# 	*
# FROM
# 	PRODUCTO p
# WHERE
# 	p.codigo IN (
# 	SELECT
# 		codigo_producto
# 	FROM
# 		DETALLE_VENTA dv
# 	WHERE
# 		dv.id_venta = '9A1A433E-F36B-1410-8BE6-006A7B6F75A4');
# declare type Perdida = {
#   id: number;
#   fecha: string;
#   producto: Producto;
#   cantidad: number;
#   total: number;
# }
def sumarCantidades(accum, detalle):
    return accum + detalle["cantidad"]
def calcularTotal(accum, detalle):
    return accum + detalle["producto"]["precio_unitario"] * detalle["cantidad"];
def get_existencias_handler(codigo):
    session = create_session()
    stmt = select(RegistroExistencia).where(RegistroExistencia.codigo_producto == codigo)
    # result = session.execute(stmt).scalars().all()
    result = session.scalars(stmt).all()
    list = []
    for r in result:
      r_dict = {
        "id": str(r.id),
        "fecha": str(r.fecha),
        "existencias": r.existencia
      }
      list.append(r_dict)
    session.close()
    return list
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
