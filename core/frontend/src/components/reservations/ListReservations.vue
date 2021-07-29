<template lang="html">
<div class="container">
    <div class="row">
        <div class="col text-left">
            <h2>Listado de Reservaciones</h2>

            <div class="col-md-12">
                <b-table striped hover :items="reservations" :fields="fields">
                    <template v-slot:cell(actions)="data">
                        <b-button size="sm" variant="primary">
                            Editar
                        </b-button>
                        <b-button size="sm" variant="danger">
                            Eliminar
                        </b-button>
                    </template>

                    

    

                </b-table>
            </div>
        </div>
    </div>
</div>
    
</template>

<script>
import axios from 'axios';

export default {  
    data () {
        return {
            fields:[
                { key: 'folio', label: 'Folio'},
                { key: 'usuario', label: 'Usuario'},
                { key: 'dia', label: 'Día'},
                { key: 'hora', label: 'Hora'},
                { key: 'mesa', label: 'Mesa'},
                { key: 'ubicacion', label: 'Ubicación'},
                { key: 'restaurante', label: 'Restaurante'},
                { key: 'facturar', label: 'Facturar'},
                { key: 'actions', label: 'Accion'},

                
            ],
            reservations:[
                {}
            ]
        }
    },
    methods: {
        
        getReservations () {
            const path = 'http://127.0.0.1:8000/api/v1.0/reservacion/?format=json'
            axios.get(path).then((response) => {
                this.reservations = response.data

            })
            .catch((error)=> {
                console.log(error)
            })
        }
    },

    created(){
        this.getReservations()
    }
}
</script>
<style lang="css" scoped>
</style>