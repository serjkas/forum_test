<template>
    <div class="table-responsive">
    <table class="table table-striped table-sm">
        <thead>
        <tr>
            <th>username</th>
            <th>forum</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="user in users" :key="user.id">
            <td>{{ user.username}}</td>  
            <td>{{ user.name}}</td>  
            

        </tr>
        
        </tbody>
    </table>
    </div>

</template>

<script>
import {ref, onMounted} from 'vue'
import axios from 'axios'

export default {
    name: "Users",
    setup() {
        const users = ref([])

        onMounted(async () => {
            const response = await axios.get('get_users_forum')   
            users.value = response.data
            console.log(response.data)
        })

        return {
            users
        }
    },
}
</script>
