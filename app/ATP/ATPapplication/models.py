# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Assotiationtennisplayers(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=30)  # Field name made lowercase.
    organizationinformation = models.TextField(db_column='OrganizationInformation')  # Field name made lowercase.
    logo = models.CharField(db_column='Logo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    face = models.CharField(db_column='Face', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'assotiationtennisplayers'


class Director(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    divisioncontinent = models.ForeignKey('Divisioncontinent', models.DO_NOTHING, db_column='DivisionContinent_ID')  # Field name made lowercase.
    fio = models.CharField(db_column='FIO', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'director'



class Divisioncontinent(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    assotiationtennisplayers = models.ForeignKey(Assotiationtennisplayers, models.DO_NOTHING, db_column='AssotiationTennisPlayers_ID')  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=100)  # Field name made lowercase.
    adress = models.CharField(db_column='Adress', unique=True, max_length=100)  # Field name made lowercase.
    telephone = models.CharField(db_column='Telephone', max_length=100)  # Field name made lowercase.
    fax = models.CharField(db_column='FAX', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'divisioncontinent'

class Game(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    grandslamtournament = models.ForeignKey('Grandslamtournament', models.DO_NOTHING, db_column='GrandSlamTournament_ID')  # Field name made lowercase.
    numberround = models.CharField(db_column='NumberRound', max_length=30)  # Field name made lowercase.
    player1 = models.ForeignKey('Player', models.DO_NOTHING, related_name='homePlayer', db_column='Player1_ID')  # Field name made lowercase.
    player2 = models.ForeignKey('Player', models.DO_NOTHING, related_name='awayPlayer', db_column='Player2_ID')  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=30)  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=30)  # Field name made lowercase.
    score = models.CharField(db_column='Score', max_length=30)  # Field name made lowercase.
    
    def scoreAsTwoList(self):
        firstString = []
        secondString = []
        listSets = self.score.split(',')
        firstString.append(listSets[0].split(':')[0])
        secondString.append(listSets[0].split(':')[1])
        for i in range(1,len(listSets)):
            currentSet = listSets[i].split('-')
            firstString.append(currentSet[0])
            secondString.append(currentSet[1])
        return firstString, secondString

    class Meta:
        managed = False
        db_table = 'game'


class Grandslamtournament(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    assotiationtennisplayers = models.ForeignKey(Assotiationtennisplayers, models.DO_NOTHING, db_column='AssotiationTennisPlayers_ID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30)  # Field name made lowercase.
    place = models.CharField(db_column='Place', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dates = models.CharField(db_column='Dates', max_length=30)  # Field name made lowercase.
    numberparticipants = models.IntegerField(db_column='NumberParticipants')  # Field name made lowercase.
    cover = models.CharField(db_column='Cover', max_length=30)  # Field name made lowercase.
    picture = models.CharField(db_column='Picture', max_length=100, blank=True, null=True)  # Field name made lowercase.
    prize = models.IntegerField(db_column='Prize')  # Field name made lowercase.
    description = models.TextField(db_column='description')   # Field name made lowercase.
    flag = models.TextField(db_column='Flag')   # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'grandslamtournament'


class News(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    assotiationtennisplayers = models.IntegerField(db_column='AssotiationTennisPlayers_ID')  # Field name made lowercase.
    textnews = models.TextField(db_column='TextNews')  # Field name made lowercase.
    photo = models.CharField(db_column='Photo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shortDescription = models.TextField(db_column='shortDescription') 

    class Meta:
        managed = False
        db_table = 'news'


class Player(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    fio = models.CharField(db_column='FIO', max_length=100)  # Field name made lowercase.
    agedatebirth = models.CharField(db_column='AgeDateBirth', max_length=100)  # Field name made lowercase.
    photo = models.CharField(db_column='Photo', max_length=100)  # Field name made lowercase.
    positionrating = models.IntegerField(db_column='PositionRating')  # Field name made lowercase.
    nationality = models.CharField(db_column='Nationality', max_length=30)  # Field name made lowercase.
    flag = models.CharField(db_column='Flag', max_length=100)  # Field name made lowercase.
    countpoints = models.IntegerField(db_column='CountPoints')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'player'


class Sponsor(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    assotiationtennisplayers = models.ForeignKey(Assotiationtennisplayers, models.DO_NOTHING, db_column='AssotiationTennisPlayers_ID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30)  # Field name made lowercase.
    picture = models.CharField(db_column='Picture', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sponsor'


class Stadium(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    grandslamtournament = models.ForeignKey(Grandslamtournament, models.DO_NOTHING, db_column='GrandSlamTournament_ID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    picture = models.TextField(db_column='Picture', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stadium'



class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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