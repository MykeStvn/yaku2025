# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Asistencia(models.Model):
    id_asi = models.AutoField(primary_key=True)
    fk_id_eve = models.ForeignKey('Evento', models.DO_NOTHING, db_column='fk_id_eve', blank=True, null=True)
    fk_id_soc = models.ForeignKey('Socio', models.DO_NOTHING, db_column='fk_id_soc', blank=True, null=True)
    tipo_asi = models.CharField(max_length=100, blank=True, null=True)
    valor_asi = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    atraso_asi = models.CharField(max_length=25)
    valor_atraso_asi = models.DecimalField(max_digits=10, decimal_places=2)
    creacion_asi = models.DateTimeField(blank=True, null=True)
    actualizacion_asi = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asistencia'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Comunicado(models.Model):
    id_com = models.AutoField(primary_key=True)
    fecha_com = models.DateField()
    mensaje_com = models.CharField(max_length=200)
    actualizacion_com = models.DateTimeField(blank=True, null=True)
    creacion_com = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comunicado'


class Configuracion(models.Model):
    id_con = models.AutoField(primary_key=True)
    nombre_con = models.CharField(max_length=250)
    ruc_con = models.CharField(max_length=13)
    logo_con = models.CharField(max_length=200, blank=True, null=True)
    telefono_con = models.CharField(max_length=50)
    direccion_con = models.CharField(max_length=50)
    email_con = models.CharField(max_length=50)
    servidor_con = models.CharField(max_length=50)
    puerto_con = models.CharField(max_length=50)
    password_con = models.CharField(max_length=50)
    creacion_con = models.DateTimeField(blank=True, null=True)
    actualizacion_con = models.DateTimeField(blank=True, null=True)
    anio_inicial_con = models.CharField(max_length=15, blank=True, null=True)
    mes_inicial_con = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'configuracion'


class Consumo(models.Model):
    id_consumo = models.AutoField(primary_key=True)
    anio_consumo = models.IntegerField(blank=True, null=True)
    mes_consumo = models.CharField(max_length=25, blank=True, null=True)
    estado_consumo = models.CharField(max_length=50, blank=True, null=True)
    fecha_creacion_consumo = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion_consumo = models.DateTimeField(blank=True, null=True)
    numero_mes_consumo = models.IntegerField(blank=True, null=True)
    fecha_vencimiento_consumo = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consumo'


class Detalle(models.Model):
    id_det = models.AutoField(primary_key=True)
    fk_id_lec = models.ForeignKey('Lectura', models.DO_NOTHING, db_column='fk_id_lec', blank=True, null=True)
    fk_id_rec = models.ForeignKey('Recaudacion', models.DO_NOTHING, db_column='fk_id_rec', blank=True, null=True)
    cantidad_det = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    detalle_det = models.CharField(max_length=1500, blank=True, null=True)
    valor_unitario_det = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    subtotal_det = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    iva_det = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detalle'

    def __str__(self):
        return self.detalle_det


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Evento(models.Model):
    id_eve = models.AutoField(primary_key=True)
    descripcion_eve = models.TextField(blank=True, null=True)
    fecha_hora_eve = models.DateTimeField(blank=True, null=True)
    lugar_eve = models.CharField(max_length=250, blank=True, null=True)
    fk_id_te = models.ForeignKey('TipoEvento', models.DO_NOTHING, db_column='fk_id_te', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evento'


class Excedente(models.Model):
    id_ex = models.AutoField(primary_key=True)
    id_tar = models.ForeignKey('Tarifa', models.DO_NOTHING, db_column='id_tar', blank=True, null=True)
    limite_minimo_ex = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    limite_maximo_ex = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tarifa_ex = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_actualizacion_ex = models.DateTimeField(blank=True, null=True)
    fecha_creacion_ex = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'excedente'


class HistorialPropietario(models.Model):
    id_his = models.AutoField(primary_key=True)
    fk_id_med = models.ForeignKey('Medidor', models.DO_NOTHING, db_column='fk_id_med', blank=True, null=True)
    fk_id_soc = models.ForeignKey('Socio', models.DO_NOTHING, db_column='fk_id_soc', blank=True, null=True)
    actualizacion_his = models.DateTimeField(blank=True, null=True)
    estado_his = models.CharField(max_length=50, blank=True, null=True)
    observacion_his = models.TextField(blank=True, null=True)
    fecha_cambio_his = models.DateTimeField(blank=True, null=True)
    creacion_his = models.DateTimeField(blank=True, null=True)
    propietario_actual_his = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'historial_propietario'


class Impuesto(models.Model):
    id_imp = models.AutoField(primary_key=True)
    nombre_imp = models.CharField(max_length=100, blank=True, null=True)
    descripcion_imp = models.TextField(blank=True, null=True)
    porcentaje_imp = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    retencion_imp = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    estado_imp = models.CharField(max_length=50, blank=True, null=True)
    creacion_imp = models.DateTimeField(blank=True, null=True)
    actualizacion_imp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'impuesto'


class Lectura(models.Model):
    id_lec = models.AutoField(primary_key=True)
    anio_lec = models.IntegerField(blank=True, null=True)
    mes_lec = models.CharField(max_length=25, blank=True, null=True)
    estado_lec = models.CharField(max_length=50, blank=True, null=True)
    lectura_anterior_lec = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    lectura_actual_lec = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_creacion_lec = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion_lec = models.DateTimeField(blank=True, null=True)
    fk_id_his = models.ForeignKey(HistorialPropietario, models.DO_NOTHING, db_column='fk_id_his', blank=True, null=True)
    fk_id_consumo = models.ForeignKey(Consumo, models.DO_NOTHING, db_column='fk_id_consumo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lectura'

    def __str__(self):
        return f"{self.anio_lec} {self.mes_lec} {self.fk_id_his.fk_id_soc}"


class Medidor(models.Model):
    id_med = models.AutoField(primary_key=True)
    fk_id_rut = models.ForeignKey('Ruta', models.DO_NOTHING, db_column='fk_id_rut', blank=True, null=True)
    fk_id_tar = models.ForeignKey('Tarifa', models.DO_NOTHING, db_column='fk_id_tar', blank=True, null=True)
    numero_med = models.CharField(max_length=50, blank=True, null=True)
    serie_med = models.CharField(max_length=100, blank=True, null=True)
    marca_med = models.CharField(max_length=100, blank=True, null=True)
    observacion_med = models.TextField(blank=True, null=True)
    estado_med = models.CharField(max_length=25, blank=True, null=True)
    foto_med = models.CharField(max_length=500, blank=True, null=True)
    creacion_med = models.DateTimeField(blank=True, null=True)
    actualizacion_med = models.DateTimeField(blank=True, null=True)
    lectura_inicial_med = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medidor'

    def __str__(self):
        return self.numero_med


class Perfil(models.Model):
    id_per = models.AutoField(primary_key=True)
    nombre_per = models.CharField(max_length=50, blank=True, null=True)
    descripcion_per = models.TextField(blank=True, null=True)
    estado_per = models.CharField(max_length=25, blank=True, null=True)
    creacion_per = models.DateTimeField(blank=True, null=True)
    actualizacion_per = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perfil'

    def __str__(self):
        return self.nombre_per


class Recaudacion(models.Model):
    id_rec = models.AutoField(primary_key=True)
    numero_factura_rec = models.CharField(max_length=250, blank=True, null=True)
    numero_autorizacion_rec = models.CharField(max_length=500, blank=True, null=True)
    fecha_hora_autorizacion_rec = models.DateTimeField(blank=True, null=True)
    ambiente_rec = models.CharField(max_length=50, blank=True, null=True)
    emision_rev = models.CharField(max_length=50, blank=True, null=True)
    clave_acceso_rec = models.CharField(max_length=500, blank=True, null=True)
    email_rec = models.CharField(max_length=500, blank=True, null=True)
    observacion_rec = models.CharField(max_length=500, blank=True, null=True)
    fk_id_soc = models.ForeignKey('Socio', models.DO_NOTHING, db_column='fk_id_soc', blank=True, null=True)
    nombre_rec = models.CharField(max_length=500, blank=True, null=True)
    identificacion_rec = models.CharField(max_length=15, blank=True, null=True)
    direccion_rec = models.CharField(max_length=500, blank=True, null=True)
    estado_rec = models.CharField(max_length=50, blank=True, null=True)
    fecha_emision_rec = models.DateTimeField(blank=True, null=True)
    fecha_creacion_rec = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion_rec = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recaudacion'


class Ruta(models.Model):
    id_rut = models.AutoField(primary_key=True)
    nombre_rut = models.CharField(max_length=500, blank=True, null=True)
    descripcion_rut = models.TextField(blank=True, null=True)
    estado_rut = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ruta'

    def __str__(self):
        return f"Ruta: {self.nombre_rut}"


class Socio(models.Model):
    id_soc = models.AutoField(primary_key=True)
    tipo_soc = models.CharField(max_length=25, blank=True, null=True)
    identificacion_soc = models.CharField(max_length=13, blank=True, null=True)
    primer_apellido_soc = models.CharField(max_length=500, blank=True, null=True)
    segundo_apellido_soc = models.CharField(max_length=500, blank=True, null=True)
    nombres_soc = models.CharField(max_length=500, blank=True, null=True)
    email_soc = models.CharField(max_length=500, blank=True, null=True)
    foto_soc = models.CharField(max_length=500, blank=True, null=True)
    telefono_soc = models.CharField(max_length=15, blank=True, null=True)
    direccion_soc = models.CharField(max_length=500, blank=True, null=True)
    fecha_nacimiento_soc = models.DateField(blank=True, null=True)
    discapacidad_soc = models.CharField(max_length=25, blank=True, null=True)
    fk_id_usu = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='fk_id_usu', blank=True, null=True)
    estado_soc = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socio'

    def __str__(self):
        return self.nombres_soc + " " + self.primer_apellido_soc + " " + self.segundo_apellido_soc

class Tarifa(models.Model):
    id_tar = models.AutoField(primary_key=True)
    nombre_tar = models.CharField(max_length=500, blank=True, null=True)
    descripcion_tar = models.TextField(blank=True, null=True)
    estado_tar = models.CharField(max_length=25, blank=True, null=True)
    m3_maximo_tar = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tarifa_basica_tar = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tarifa_excedente_tar = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    valor_mora_tar = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tarifa'

    def __str__(self):
        return self.nombre_tar


class TipoEvento(models.Model):
    id_te = models.AutoField(primary_key=True)
    nombre_te = models.CharField(max_length=150, blank=True, null=True)
    estado_te = models.CharField(max_length=50, blank=True, null=True)
    creacion_te = models.DateTimeField(blank=True, null=True)
    actualizacion_te = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_evento'


class Usuario(models.Model):
    id_usu = models.AutoField(primary_key=True)
    apellido_usu = models.CharField(max_length=150, blank=True, null=True)
    nombre_usu = models.CharField(max_length=150, blank=True, null=True)
    email_usu = models.CharField(max_length=150, blank=True, null=True)
    password_usu = models.CharField(max_length=500, blank=True, null=True)
    estado_usu = models.CharField(max_length=25, blank=True, null=True)
    fk_id_per = models.ForeignKey(Perfil, models.DO_NOTHING, db_column='fk_id_per', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'

    def __str__(self):
        return self.nombre_usu + " " + self.apellido_usu
