<template>
<div>
    <Navbar/>
    <Users />
</div>    
</template>


<script>
import Navbar from  "@/components/Navbar.vue"
import Users from  "@/components/Users.vue"

export default {
    name: "Main",
    components: {
        Navbar,
        Users
    }
}
</script>