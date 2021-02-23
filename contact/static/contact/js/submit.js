function addEvent(){
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    const csrftoken = getCookie('csrftoken');

    el = document.getElementById("sub-btn");
    el.onclick = (e)=>{
        // e.preventDefault()
        const f_name = document.getElementById('name'),
         email = document.getElementById('email'),
         skype_id = document.getElementById('skype'),
         countries = document.getElementById('countries'),
         orders = document.getElementById('orders'),
         product = document.getElementById('product'),
         message = document.getElementById('message'),
         data={
            f_name:f_name,
            email:email,
            skype_id:skype_id,
            countries:countries,
            orders:orders,
            message:message,
            product:product,
         },
         URL = 'http://127.0.0.1:8800/send-order/',
         options={
             credentials: 'same-origin',
             method:"POST",
             headers:{
                'X-CSRFToken': csrftoken,
                'Accept': 'application/json',
             },
             body:JSON.stringify(data),
         }

         fetch(URL, options)
         .then((response)=>{
             return response.json()
         }).then((data)=>{
             console.log(data.message)
         })

    }

}
addEvent();