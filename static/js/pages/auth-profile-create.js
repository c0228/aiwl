/* ------ PERSONAL DETAILS ::: START ----------------------------------------------- */
const LOAD_CREATEPROFILE_LEFTMENUDATA = [{
    id: "personal_details",
    name: "Personal Details",
    view: "createProfile_formDisplay_personalDetails"
 },{
    id: "edu_qualifications",
    name: "Educational Qualifications",
    view: "createProfile_formDisplay_eduDetails"
 },{
    id: "emp_details",
    name: "Employer's Details",
    view: "createProfile_formDisplay_empDetails"
 },{
    id: "visa_details",
    name: "Visa Details",
    view: "createProfile_formDisplay_visaDetails"
 },{
    id: "tech_stack_details",
    name: "Tech Stack Details",
    view: "createProfile_formDisplay_techStackDetails"
 }];
function sel_createProfile_leftMenu(activeId){
 for(let i=0;i<LOAD_CREATEPROFILE_LEFTMENUDATA?.length;i++){
    const menuId = LOAD_CREATEPROFILE_LEFTMENUDATA[i]?.id;
    const view = LOAD_CREATEPROFILE_LEFTMENUDATA[i]?.view;
    if(activeId===menuId){
        $('#'+menuId).removeClass('disabled');
        $('#'+menuId).addClass('active fWBold');
        document.getElementById(view).style.display='block';
    } else {
        $('#'+menuId).removeClass('active fWBold');
        $('#'+menuId).addClass('disabled');
        document.getElementById(view).style.display='none';
    }
 }
}
function load_createProfile_leftMenu(id, activeId) {
 let menuView;
 let content='<ul class="nav nav-pills flex-column">';
    for(let i=0;i<LOAD_CREATEPROFILE_LEFTMENUDATA?.length;i++){
        const menuId = LOAD_CREATEPROFILE_LEFTMENUDATA[i]?.id;
        const menuName = LOAD_CREATEPROFILE_LEFTMENUDATA[i]?.name;
        content+='<li class="nav-item">';
        if(activeId===menuId) {
            menuView = LOAD_CREATEPROFILE_LEFTMENUDATA[i]?.view;
            content+='<a id="'+menuId+'" class="nav-link active fWBold" href="#">'+menuName+'</a>';
        } else {
            content+='<a id="'+menuId+'" class="nav-link disabled" href="#">'+menuName+'</a>';
        }
        content+='</li>';
    }
    content+='</ul>';
 document.getElementById(id).innerHTML = content;
 document.getElementById(menuView).style.display='block';
}
function save_createProfile_personalDetails(){
 document.getElementById("createProfile_formNextBtn_personalDetails").style.display='inline-block';
}
function next_createProfile_personalDetails(){
 sel_createProfile_leftMenu('edu_qualifications');
}
/* ------ PERSONAL DETAILS ::: END ----------------------------------------------- */
/* ------ EDUCATIONAL QUALIFICATIONS ::: START ----------------------------------- */
function previous_createProfile_eduDetails(){
 sel_createProfile_leftMenu('personal_details');
 document.getElementById("createProfile_formNextBtn_personalDetails").style.display='none';
}
function save_createProfile_eduDetails(){
 document.getElementById("createProfile_formNextBtn_eduDetails").style.display='inline-block';
}
function next_createProfile_eduDetails(){
 sel_createProfile_leftMenu('emp_details');
}
/* ------ EDUCATIONAL QUALIFICATIONS ::: END ----------------------------------- */
/* ------ EMPLOYEE'S DETAILS ::: START ----------------------------------- */
function previous_createProfile_empDetails(){
 sel_createProfile_leftMenu('edu_qualifications');
 document.getElementById("createProfile_formNextBtn_eduDetails").style.display='none';
}
function save_createProfile_empDetails(){
 document.getElementById("createProfile_formNextBtn_empDetails").style.display='inline-block';
}
function next_createProfile_empDetails(){
 sel_createProfile_leftMenu('visa_details');
 load_countries_list("createProfiles_visaWorkAuth");
}
/* ------ EMPLOYEE'S DETAILS ::: END ----------------------------------- */
/* ------ VISA DETAILS ::: START ----------------------------------- */
function previous_createProfile_visaDetails(){
 sel_createProfile_leftMenu('emp_details');
 document.getElementById("createProfile_formNextBtn_empDetails").style.display='none';
}
function save_createProfile_visaDetails(){
 document.getElementById("createProfile_formNextBtn_visaDetails").style.display='inline-block';
}
function next_createProfile_visaDetails(){
 sel_createProfile_leftMenu('tech_stack_details');
}
/* ------ VISA DETAILS ::: END ----------------------------------- */
/* ------ TECH STACK DETAILS ::: START ----------------------------------- */
function previous_createProfile_techStackDetails(){
 sel_createProfile_leftMenu('visa_details');
 document.getElementById("createProfile_formNextBtn_visaDetails").style.display='none';
 document.getElementById("createProfile_formNextBtn_techStackDetails").style.display='none';
}
function save_createProfile_techStackDetails(){
 document.getElementById("createProfile_formNextBtn_techStackDetails").style.display='inline-block';
}
function publish_createProfile_techStackDetails(){
 
}
/* ------ TECH STACK DETAILS ::: END ----------------------------------- */