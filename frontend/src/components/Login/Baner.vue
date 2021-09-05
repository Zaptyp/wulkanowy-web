<template>
    <div class="card" style="float: left;">
        <v-col>
           <v-row align="center">
              <v-card dark color="#d32f2f" style="height: 524px; margin-right: 35px; width: 350px;">
                <v-card-text>
                  <div style="width: 140; height: 140;">
                    <img src="../../assets/wulkanowy.svg"
                    width="140"
                    class="logo"/>
                  </div>
                <div id="headlineRed">Wulkanowy</div>
                <div id="headlineTwo">Nieoficjalna aplikacja przeglądarkowa ucznia i
                  rodzica dla dziennika Vulcan UONET+
                  </div>
                <br><br><br>
                <a href="#" target="_blank" style="color: white;">Polityka prywatności</a>
                <br>
                <div id="headlineTwo">v 0.1.0</div>
                </v-card-text>
              </v-card>
           </v-row>
        </v-col>
    </div>
</template>
<style>
.cardTwo{
  float: left;
  height: 500px;
  top: 5%;
  margin-bottom: 50px;
  width: 450px;
}
#headlineRed{
  text-align: center;
  font-weight: 300;
  font-size: 2pc;
  margin-bottom: 1pc;
  color: white;
  font-weight: 400;
  text-shadow: -1px 2px 0px rgba(157,0,0,0.73);
  margin-top: 10px;
}

#headlineTwo{
  text-align: center;
  font-weight: 300;
  font-size: 1pc;
  margin-bottom: 1.5pc;
  color: white;
  padding: 10px;
}
.logo img{
  text-shadow: -1px 2px 0px rgba(157,0,0,0.73);
}
</style>
