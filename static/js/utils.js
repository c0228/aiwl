function getCurrentTimestampFormatted() {
  const now = new Date();

  const year = now.getFullYear();
  const month = String(now.getMonth() + 1).padStart(2, '0'); // Months are 0-indexed
  const day = String(now.getDate()).padStart(2, '0');
  const hours = String(now.getHours()).padStart(2, '0');
  const minutes = String(now.getMinutes()).padStart(2, '0');
  const seconds = String(now.getSeconds()).padStart(2, '0');

  return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
}

function api_executor(url, func){
 fetch(url)
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok ' + response.statusText);
    }
    return response.json(); // parse JSON response
  })
  .then(data => { 
	func(data);
  });
}

function load_select_options(id, label, data){
 let content = '<option value="">'+label+'</option>';
	for(let i=0;i<data.length;i++){
		content+='<option value="'+data[i]+'">'+data[i]+'</option>';
	}
	document.getElementById(id).innerHTML = content;
}

function load_countries_list(id){
 api_executor('http://localhost/apis/get/countries/list',(data)=>{
	load_select_options('register_countries', 'Select your Country', data);
 });
}

function load_states_list(){
 const country = document.getElementById("register_countries").value;
 const status = (country.length>0)?'block':'none';
 document.getElementById("mod_register_states").style.display = status;
 api_executor('http://localhost/apis/get/'+country+'/states',(data)=>{
	document.getElementById("register_mobile_index").innerHTML = data?.["tel_index"];
	load_select_options('register_states', 'Select your State', data?.["states"]);
 });
}

function load_form_alert(id,type,data){
 let content='<div class="alert alert-'+type+' alert-dismissible">';
	content+='<button type="button" class="btn-close" data-bs-dismiss="alert"></button>';
	content+=data;
	content+='</div>';
 document.getElementById(id).innerHTML = content;
}
