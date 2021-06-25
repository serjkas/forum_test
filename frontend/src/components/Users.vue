<template>
<div>
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

    <nav aria-label="Page navigation example">
    <ul class="pagination">
        <li class="page-item"><a class="page-link" @click="prev">Previous</a></li>
        <li class="page-item"><a class="page-link" @click="next">Next</a></li>
    </ul>
    </nav>
</div>
</template>

<script>
import {ref, onMounted} from 'vue'
import axios from 'axios'

export default {
    name: "Users",
    setup() {
        const users = ref([])
        const page = ref(1)

        const load = async () => {
            
            const response = await axios.get(`get_users_forum?page=${page.value}`)   
            users.value = response.data.results
            console.log(users.value)
        }
        onMounted(load)

        const next = async () => {
            page.value++
            await load()
        }

        const prev = async () => {
            page.value--
            await load()
        }

        return {
            users,
            next,
            prev
        }
    },
}
</script>
