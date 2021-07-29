<template>
  <div >
    <b-container>

      <div class="col text-left">
                <h2>Editar Reservacion</h2>
            </div>

        <div class="row">
            <div class="col">
                <div class="card">
                    <div class="card-body">

                        <form @onSubmit="onSubmit">

                            <div class="form-group row">
                                <label for="title" class="col-sm-2 col-form-label">Folio</label>
                                <div class="col-sm-6">
                                    <input type="text" placeholder="Folio" name="folio" class="form-control" v-model.trim="form.folio">
                                </div>
                            </div>

                        </form>
                        <form @onSubmit="onSubmit">

                            <div class="form-group row">
                                <label for="title" class="col-sm-2 col-form-label">Usuario</label>
                                <div class="col-sm-6">
                                    <input type="text" placeholder="Usuario" name="usuario" class="form-control" v-model.trim="form.usuario">
                                </div>
                            </div>

                        </form>
                        <form @onSubmit="onSubmit">

                            <div class="form-group row">
                                <label for="title" class="col-sm-2 col-form-label">Día</label>
                                <div class="col-sm-6">
                                    <input type="date" placeholder="Día" name="dia" class="form-control" v-model.trim="form.dia">
                                </div>
                            </div>

                        </form>
                        <form @onSubmit="onSubmit">

                            <div class="form-group row">
                                <label for="title" class="col-sm-2 col-form-label">Hora</label>
                                <div class="col-sm-6">
                                    <b-form-select v-model="form.hora" ></b-form-select>
                                </div>
                            </div>

                        </form>
                        <form @onSubmit="onSubmit">

                            <div class="form-group row">
                                <label for="title" class="col-sm-2 col-form-label">Mesa</label>
                                <div class="col-sm-6">
                                    <b-form-select v-model="selected" :options="form.mesa" ></b-form-select>
                                </div>
                            </div>

                        </form>
                        <form @onSubmit="onSubmit">

                            <div class="form-group row">
                                <label for="title" class="col-sm-2 col-form-label">Ubicación</label>
                                <div class="col-sm-6">
                                    <b-form-select v-model="selected" :options="form.ubicacion" ></b-form-select>
                                </div>
                            </div>

                        </form>
                        <form @onSubmit="onSubmit">

                            <div class="form-group row">
                                <label for="title" class="col-sm-2 col-form-label">Restaurante</label>
                                <div class="col-sm-6">
                                    <b-form-select v-model="selected" :options="form.restaurante" ></b-form-select>
                                </div>
                            </div>

                        </form>
                        <form @onSubmit="onSubmit">

                            <div class="form-group row">
                                <label for="title" class="col-sm-2 col-form-label"></label>
                                <div class="col-sm-6">
                                     <input type="checkbox" placeholder="Día" name="dia" class="form-control" v-model.trim="form.facturar">
                                </div>
                            </div>

                            <div class="rows">
                                <div class="col text-left">
                                    <b-button type="submit" variant="primary">Editar</b-button>
                                    <b-button type="submit" class="btn-large" variant="danger" :to="{ name: 'ListReservation'}">Cancelar</b-button>
                                </div>

                            </div>


                        </form>

                        

                    </div>
                </div>
            </div>
        </div>
   
    </b-container>

  </div>
</template>
<script>
import axios from 'axios'
export default {
    data() {
        return {
            reservacionId: this.$route.params.reservacionId,
            form: {
                folio: '',
                usuario: '',
                dia: '',
                hora: '',
                mesa: '',
                ubicacion: '',
                restaurante: '',
                facturar: '',
            }
        }
    },
    methods: {
        onSubmit(event){
            event.preventDefault
        },

        getReservation () {
            const path = `http://127.0.0.1:8000/api/v1.0/reservacion/${this.reservacionId}/`

            axios.get(path).then((response) =>{

                this.form.folio = response.data.folio
                this.form.usuario = response.data.usuario
                this.form.dia = response.data.dia
                this.form.hora = response.data.hora
                this.form.mesa = response.data.mesa
                this.form.ubicacion = response.data.ubicacion
                this.form.restaurante = response.data.restaurante
                this.form.facturar = response.data.facturar
            })
            .catch((response) => {
                console.log(error)
            })
        }
    },
    created() {
        this.getReservation()
    },
}
</script>
<style lang="css" scoped>
</style>