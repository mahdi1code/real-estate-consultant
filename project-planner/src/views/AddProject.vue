<template>
    <form @submit.prevent="HandelSubmit">
        <label>Title :</label>
        <input v-model="title" type="text" required>
        <label>Details :</label>
        <textarea v-model="details"></textarea>
        <button>Add Project</button>
    </form>

</template>

<script>

export default{
    data () {
        return{
            title: '',
            details: '',
        }
    },
     methods:{
        HandelSubmit () {
            let Project = {
                title : this.title, 
                details : this.details,
                complete : false,
            }
            fetch('http://localhost:3000/projects', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(Project)
            })
                
        }
     }
}

</script>

<style>

form{
    background: whitesmoke;
    padding: 20px;
    border-radius: 10px;
}

label{
    display: block;
    color: #bbb;
    text-transform: uppercase;
    font-size: 14px;
    font-weight: bold;
    letter-spacing: 1px;
    margin: 20px 10px 0;
}

input{
    padding: 10px;
    border: 0px;
    border-bottom: 10px solid #ddd;
    width: 100%;
    box-sizing: border-box;
}

textarea{
    border: 1px solid #ddd;
    padding: 10px;
    width: 100%;
    box-sizing: border-box;
    height: 100%;
}

form button{
    display: block;
    margin: 20px auto 0;
    background: #00ce89;
    color:whitesmoke;
    padding: 10px;
    border: 0;
    border-radius: 6px;
    font-size: 16px;
}

</style>