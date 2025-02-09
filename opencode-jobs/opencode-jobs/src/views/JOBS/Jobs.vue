<template>
    <div>
        <div v-if="jobs.length">
            <h1>Jobs</h1>
            <div v-for="job in jobs" :key="job.id" class="job">
                <router-link :to="{name : 'JobsDeteils', params:{id: job.id}}"> {{ job.title }} </router-link>
            </div>
        </div>
        <div v-else><p>Jobs Details Loading...</p></div>
    </div>
</template>

<script>

export default {
    data () {
        return {
            jobs : []
        }
    },
    mounted () {
        fetch('http://localhost:3000/jobs')
            .then(res => res.json())
            .then(data => this.jobs = data)
            .then(err => console.log(err.message))
    }
}

</script>

<style>

.job {
    background: whitesmoke;
    padding: 20px;
    border-radius: 10px;
    margin: 10px auto;
    max-width: 600px;
    cursor: pointer;
    color: #444;
}

.job:hover {
    background: wheat;
}

.job a {
    text-decoration: none;
}
</style>