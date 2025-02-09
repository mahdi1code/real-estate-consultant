<template>
    <div>
        <div v-if="job"> 
            <h1>{{ job.title }}</h1>
            <p>route id is {{ id }}</p>
            <p>{{ job.details }}</p>
        </div>
        <div v-else>
            <p>Jobs Details Loading...</p>
        </div>
    </div>
</template>

<script>
export default{
    props: ['id'],

    data () {
        return {
            job : null
        }
    },

    mounted () {
        fetch('http://localhost:3000/jobs/' + this.id)
            .then(res => res.json())
            .then(data => this.job = data)
            .then(err => console.log(err.message))
    }
}
</script>

<style>

</style>