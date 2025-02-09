<template>

    <div>
        <form @submit.prevent="HandelSubmit">
            <label>Email : </label>
            <input type="email" required v-model="email">

            <label>Password : </label>
            <input type="Password" required v-model="Password">
            <div v-if="passwordError" class="error">{{ passwordError }}</div>

            <label>Role :</label>
            <select v-model="role">
                <option value="developer">web developer</option>
                <option value="designer">web Designer</option>
            </select>

            <label>Skills (alt)</label>
            <input type="text" v-model="tempSkill" @keyup.alt="addSkill">
            <div v-for="item in Skills" :key="item" class="pill">
                <span @click="deleteSkill(item)">{{ item }}</span>
            </div>

            <div class="terms">
                <input type="checkbox" v-model="terms" required>
                <label>Accept Terms and Conditions</label>
            </div>

            <button type="submit">Create an Account</button>
            <div class="submit">
            </div>

        </form>
        <p>Email : {{ email }}</p>
        <p>Password : {{ Password }}</p>
        <p>Role : {{ role }}</p>
        <p>Terms : {{ terms }}</p>
        <p>Skills : {{ Skills }}</p>
        <!-- <p>Names : {{ names }}</p> -->
    </div>
</template>

<script>
export default {
    data() {
        return {
            email : '',
            Password : '',
            role : '',
            terms : false,
            // names : [],
            tempSkill : '',
            Skills : [],
            passwordError : ''
        }
    },
    methods : {
        addSkill (e) {
            if (e.key === ',' && this.tempSkill) {
                if (!this.Skills.includes(this.tempSkill)) {
                    this.Skills.push(this.tempSkill)
                }
                this.tempSkill = ''
            }  
        },

        deleteSkill (item) {
            this.Skills = this.Skills.filter((i) => {
                return item !== i
            })
        },

        HandelSubmit () {
            // if(this.Password.length > 5){
            //     this.passworderror = ''
            // }else{
            //     this.passworderror = 'passwoord its not more than 5 chars'
            // }

            this.passwordError = this.Password.length > 5 ?
                ' ' : 'passwoord its not more than 5 chars'  

            if(!this.passwordError){
                console.log('email' , this.email)
                console.log('Password' , this.Password)
                console.log('role' , this.role)
                console.log('Skills' , this.Skills)
                console.log('terms Accepted' , this.terms)
            }
        }
    }
}
</script>

<style>

form {
    max-width: 400px;
    margin: 30px auto;
    background: whitesmoke;
    text-align: left;
    padding: 40px;
    border-radius: 10px;
}

label {
    color: black;
    display: inline-block;
    margin: 25px 0 15px;
    font-size: 0.6em;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: bold;
}

input, select {
    display: block;
    padding: 10px 6px;
    width: 100%;
    box-sizing: border-box;
    border: none;
    border-bottom: 1px solid #ddd;
    color:#555;
}

input[type='checkbox'] {
    display: inline-block;
    width: 16px;
    margin: 0 10px 0 0;
    position: relative;
    top:2px;
}

.pill {
    display: inline-block;
    margin: 20px 10px 0 0;
    padding: 6px 12px;
    background: #eee;
    border-radius: 20px;
    font-size: 12px;
    letter-spacing: 1px;
    font-weight: bold;
    color: #777;
    cursor: pointer;
}

button {
    background: #0b6dff;
    border: 0;
    padding: 10px 20px;
    margin-top: 20px;
    color: whitesmoke;
    border-radius: 20px;
}

.submit {
    text-align: center;
}

.error {
    color: #ff0062;
    margin-top: 10px;
    font-size: 0.8em;
    font-weight: bold;
}
</style>


<!-- <div>
                <input type="checkbox" value="mahdi" v-model="names">
                <label>mahdi</label>
            </div>

            <div>
                <input type="checkbox" value="nader" v-model="names">
                <label>nader</label>
            </div>

            <div>
                <input type="checkbox" value="bahram" v-model="names">
                <label>bahram</label>
            </div> -->