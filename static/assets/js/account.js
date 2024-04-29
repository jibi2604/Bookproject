function alertBox(){
      username = document.getElementById('username').value
      email = document.getElementById('email').value
      password = document.getElementById('password').value
      cpassword = document.getElementById('cpassword').value

      if(!username || !email || !password || !cpassword){
      alert("Please fill out all the fields")
      } else{
      alert("Registration successful")
      }
}