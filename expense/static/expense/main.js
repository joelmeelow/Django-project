const user_name = document.querySelector('#table');
const hey = document.querySelector('#you');
const email_user = document.querySelector('#email');
const user_surname = document.querySelector('#yes');
const passw = document.querySelector('#password');
const logs = document.querySelector('#log');
const logins = document.querySelector('#login');
const loginmail = document.querySelector('#loginemail');
const showsign = document.querySelector('.key');
const showp = document.querySelector('#pass');

const showpass = (e) => {
    if(showsign.textContent === 'SHOW'){
        showsign.textContent = 'HIDE';
        passw.setAttribute("type", "text");

    }else{
        showsign.textContent = 'SHOW';
        passw.setAttribute("type", "password");

    }
}

showsign.addEventListener('click', showpass)

user_name.addEventListener('keyup', (e) => {
    console.log('hope');
    const username_js = e.target.value;
    

    logs.innerHTML = '';
    logs.style.color = 'green';
if(username_js.length > 0){
    fetch("/", {
        body: JSON.stringify({firstname: username_js}),
        method: "POST"
    }).then((res) => res.json()).then((data) => { 
        console.log("data", data);
    if(data.user_error){
        logs.innerHTML = 'only alphabets!'
        logs.style.color = 'red';
    }});
}
});

user_surname.addEventListener('keyup', (e) => {
    console.log('joy');
    const surname_js = e.target.value;
    

    logins.innerHTML = '';
    logins.style.color = 'green';
if(surname_js.length > 0){
    fetch("surge", {
        body: JSON.stringify({surname: surname_js}),
        method: "POST"
    }).then((res) => res.json()).then((data2) => { 
        console.log("data2", data2);
    if(data2.user_error){
        logins.innerHTML = 'only alphabets'
        logins.style.color = 'red';
    }});
}
});
email_user.addEventListener('keyup', (e) => {
    console.log('joy');
    const useremail_js = e.target.value;
    

    loginmail.innerHTML = '';
    loginmail.style.color = 'green';
if(useremail_js.length > 0){
    fetch("post", {
        body: JSON.stringify({email: useremail_js}),
        method: "POST"
    }).then((res) => res.json()).then((data3) => { 
        console.log("data3", data3);
    if(data3.email_error){
        loginmail.innerHTML = 'enter valid email'
        loginmail.style.color = 'red';
    }});
}
});
passw.addEventListener('keyup', (e) => {
    console.log('joy');
    const password_js = e.target.value;
    

    showp.innerHTML = '';
    showp.style.color = 'green';
if(password_js.length > 0){
    fetch("passw", {
        body: JSON.stringify({password: password_js}),
        method: "POST"
    }).then((res) => res.json()).then((data4) => { 
        console.log("data4", data4);
    if(data4.password_error){
        showp.innerHTML = '> 8 cha'
        showp.style.color = 'red';
    }});
}
});