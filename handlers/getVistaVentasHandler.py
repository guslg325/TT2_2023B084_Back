import azure.functions as func
from handlers.utils import to_mx_timezone
from sqlalchemy import select, insert, update
from .models import Venta, Producto, VistaVentas
from sqlalchemy.ext.serializer import loads, dumps
from functools import reduce
import json
from functools import reduce
from .connect import create_session
from collections import defaultdict;

def get_vista_ventas_handler():
    final_result = []
    session = create_session()
    stmt = select(VistaVentas).order_by(VistaVentas.fecha.desc())
    result = session.execute(stmt).scalars().all()
    for r in result:
        final_result.append(r.as_dict())
    session.commit()
    session.close()

    grouped = defaultdict(list)

    for item in final_result:
        key = (item['id_venta'], item['fecha'])
        grouped[key].append({
            "codigo_producto": item['codigo_producto'],
            "nombre": item['nombre'],
            "cantidad": item['cantidad'],
            "registro_precio": item['registro_precio'],
            "subtotal": item['subtotal'],
        })
    final_result = [{
        "id_venta": key[0],
        "fecha": key[1],
        "items": values,
        "cantidad": reduce(lambda accum, item: accum + item["cantidad"], values, 0),
        "total": reduce(lambda accum, item: accum + item["subtotal"], values, 0)
    } for key, values in grouped.items()]
    return final_result