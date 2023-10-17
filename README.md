[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/XixB-tii)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=12362336)
# Proyecto
# Informe
## Análisis del problema:
Se nos presenta una tienda donde el cliente quiere obtener en línea la factura de sus compras. Los clientes se identificarán por medio de su RFC, donde se divide en persona física y persona moral. Estos dos en sus características solo compartirán lo que es el RFC, el correo electrónico, y aunque la física tiene su nombre, la razón social sería el nombre de la entidad que se tiene como cliente, teniendo como diferencia que el moral tiene una persona de contacto. Aquí se puede tener una clase “cliente” para encapsular todos los datos de estos dos tipos. 
El cliente va a realizar una compra, por lo tanto, se necesitarán productos que comprar para empezar, por lo tanto, se puede tener una clase “producto” que encapsulara los productos como tal y una clase “compra” para realizar los cálculos de los productos, de aquí podemos obtener una relación de composición, ya que no se puede hacer una compra sin que haya productos, y también podemos obtener una de agregación, ya que un cliente puede realizar múltiples compras. A partir de esto se tiene que obtener un recibo, por lo tanto, podemos hacer una clase “recibo” para obtenerlo, en el cual se incluirán las compras a realizar, junto con el total y el IVA. Por lo tanto, se puede obtener otra relación de composición, ya que no puede existir el recibo sin las compras a realizar (lo cual incluye los productos). Después de que el recibo haya dado un identificador se tendrá que obtener una factura, de ahí podemos sacar una clase “factura” para generarlas, tanto en formato PDF como XML, cada compra tendrá su factura, y la factura no puede existir sin que haya habido una compra, por lo tanto, se tiene otra relación de composición ahí.

## Diseño UML
![ProyectoTercerTrimestre](https://github.com/AGN-Teaching/proyecto-equipo-3/assets/125591190/45e038a5-d07d-491b-8e25-808b3a63e252)

## Descripción:  
### Clase Cliente:
#### Atributos:
- rfc: any // Mantiene registrado el rfc del cliente
- tipo : string // Mantiene registrado el tipo de cliente
- nombre: any // Mantiene registrado el nombre del cliente
- correo_electronico: any // Mantiene registrado el correo del cliente
- razon_social: any // Mantiene registrado la razón social del cliente
- persona_contacto: any // Mantiene registrado el nombre de la persona de contacto del cliente.
#### Métodos:
+ getRfc: any // Retorna el rfc del cliente
+ getTipo : string // Retorna el tipo de cliente
+ getNombre: any // Retorna el nombre del cliente
+ getCorreo_electronico: any // Retorna el correo electrónico del cliente
+ getRazon_social: any // Retorna la razón social del cliente
+ getPersona_contacto: any // Retorna el nombre de la persona de contacto del cliente

### Clase Producto:
#### Atributos:
- nombre_producto: any // Mantiene registrado el nombre del producto
- precio: float // Mantiene registrado el precio del producto
- cantidad: int // Mantiene registrado la cantidad de un producto
#### Métodos:
+ calcular_subtotal(self): float // Calcula el subtotal del producto, ósea la cantidad por el precio

### Clase Compra:
#### Atributos:
- cliente: Cliente // Crea una instancia de la clase “Cliente”
- producto: Producto // Crea una instancia de la clase “Producto”
- fecha: string // Mantiene registrado la fecha en que se hace la compra
- total: float // Mantiene registrado el total de la compra
- iva: float // Mantiene registrado el iva de la compra
#### Métodos:
+ calcular_total(self): float // Calcula el total final de la compra

### Clase Recibo:
#### Atributos:
- compra: Compra // Crea una instancia de la clase “Compra”
- identificador: string // Mantiene registrado un identificador para el recibo
#### Métodos:
+ generar_recibo(self): // Genera el recibo completo

#### Clase Factura:
#### Atributos:
- compra: Compra // Crea una instancia de la clase “Compra”
- cfid: string // Mantiene registrado el comprobante fiscal digital
##### Métodos:
+ generar_factura_pdf(self): // Genera la factura con todos los datos en pdf
+ generar_factura_xml(self): // Genera la factura con todos los datos en xml

## Conclusiones individuales:
### Ochoa De La Cruz Bryan Tonatiuh:
Este programa de sistema de facturación, a lo largo del proyecto, requirió el uso de conceptos previamente vistos, uno de los más destacables es la composición, la cual destaca sobre todo en las clases y la relación que existe en estas. Pero no es lo único que se utiliza, sino que conceptos como la encapsulación o la relación de agregación, también tienen presencia en dicho sistema. Donde cada clase creada posee los métodos que le permiten hacer la acción que este necesita. Haciendo así que cada clase tome un rol específico con el cual quede bien definida su funcionalidad.
Es gracias a todo esto que la definición de las clases y la estructura de relaciones entre ellas permiten ver de manera clara la gestión de clientes, compras, productos, recibos y facturas.
En resumen, este proyecto ilustra cómo varios conceptos de la programación orientada a objetos pueden usarse de manera conjunta para modelar un sistema complejo que a la vez puede sentar las bases de un sistema para que pueda ser ampliado y mejorado, si así se requiriera según las necesidades específicas de un sistema de facturación más complejo.
### Medrano Cano Axel Andre:
A lo largo del desarrollo de este proyecto, se han destacado conceptos fundamentales de la programación orientada a objetos, como encapsulación, composición, agregación y relaciones entre clases.
Hemos demostrado cómo modelar un sistema de facturación que involucra clientes, compras, productos, recibos y facturas, y cómo utilizar la encapsulación para controlar el acceso a los atributos de las clases. Además, se han proporcionado métodos para realizar acciones específicas y generar recibos y facturas.
Si bien esta implementación es simplificada, sienta las bases para un sistema de facturación más completo y escalable. En un contexto real, se podrían agregar más características y funcionalidades, como la gestión de inventario, registros fiscales, cálculos de impuestos y generación de archivos PDF y XML.
