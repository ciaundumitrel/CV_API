
var full_str = 0
var full_stl = 0
var full_sbl = 0
var full_sbr = 0
var full_ctr = 0
$(".split.top.left").click(function(){
    if(full_stl == 0){
        $(this).animate({height: "100%", width: "100%", fontSize: "2.5vh"});
        full_stl = 1;
        $(this).css('z-index', 3);
        $('.education_text').show();
        $('.education_instruction').hide();
        }
    else{
        $(this).animate({height: "50%", width: "50%", fontSize: "1.5vh"}).promise().done( function(){
        $('.education_text').hide();
        $('.education_instruction').show();
         $(this).css('z-index', 1);
         full_stl = 0;

        });
}
});
$(".split.top.right").click(function(){
    if(full_str == 0){
        $(this).animate({height: "100%", width: "100%", fontSize: "2.5vh"});
        full_str = 1;
        $('.experience_text').show();
        $('.professional_instruction').hide();

        $(this).css('z-index', 3);

        console.log(1)

        }
    else{
        $(this).animate({height: "50%", width: "50%", fontSize: "1.5vh"}).promise().done( function(){

         $(this).css('z-index', 1);
                 full_str = 0;
        $('.experience_text').hide();
        $('.professional_instruction').show();

        });
        }
});

$(".split.bot.left").click(function(){
    if(full_sbl == 0){
        $(this).animate({height: "100%", width: "100%", fontSize: "2.5vh"});
        full_sbl = 1;
        $('.skill_text').show();
        $('.skill_instruction').hide();
        $(this).css('z-index', 3);

        }
    else{
        $(this).animate({height: "50%", width: "50%", fontSize: "1.5vh"}).promise().done( function(){
        $('.skill_text').hide();
        $('.skill_instruction').show();

         $(this).css('z-index', 1);
            full_sbl = 0;

        });
        }
});

$(".split.bot.right").click(function(){
        if(full_sbr == 0){
        $(this).animate({height: "100%", width: "100%", fontSize: "2.5vh"});
        full_sbr = 1;
        $('.projects_text').show();
        $('.projects_instruction').hide();
        $(this).css('z-index', 3);

        }
    else{
        $(this).animate({height: "50%", width: "50%", fontSize: "1.5vh"}).promise().done( function(){

         $(this).css('z-index', 1);
         full_sbr = 0;
         $('.projects_text').hide();
         $('.projects_instruction').show();
        });
}
})

$(".central_widget").click(function(){
        if(full_sbr == 0){
        $(this).animate({height: "70%", width: "70%", fontSize: "2.5vh", "left":"15%", "top":"15%"});
        full_sbr = 1;
        $(this).css('z-index', 3);
         $('.personal_info').show();
         $('.personal_instructions').hide();
        }
    else{
        $(this).animate({height: "40%", width: "40%", fontSize: "1.5vh", "left":"30%", "top":"30%"}).promise().done( function(){

         $(this).css('z-index', 1);
        full_sbr = 0;
         $('.personal_info').hide();
         $('.personal_instructions').show();
        });

        }
});
