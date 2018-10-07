<template>
    <el-container>
        <el-header>Header</el-header>
        <el-container>
            <el-main width="50%">
                 <div class="left-container"  style="margin:auto 20%;padding-bottom: 20px;">
                    <el-card class="box-card-component" style="margin-left:8px;">
                            <div slot="header" class="box-card-header">
                              <img src="https://wpimg.wallstcn.com/e7d23d71-cf19-4b90-a1cc-f56af8c0903d.png">
                            </div>
                            <div style="position:relative;">
                              <pan-thumb :image="avatarNan" class="panThumb"/>
                              <mallki class-name="mallki-text" text="李小磊"/>
                              <div style="padding-top:35px;" class="progress-item">
                                    <el-tag>属性分评</el-tag>
                              </div>
                              <el-collapse accordion>
                                <div v-for="NanProgress in NanProgressList" class="progress-item">
                                  <el-collapse-item>
                                    <template slot="title">
                                      <span slot="reference">{{ NanProgress.attrname }}</span>
                                      <i class="header-icon el-icon-info"></i>
                                      <div style="display: inline;">
                                          <el-progress :percentage="NanProgress.progress" :status="NanProgress.status" 
                                          style="float: right;width: 70%;top:35%;"/>
                                      </div>
                                    </template>
                                    <el-card shadow="hover" class="box-card">
                                        <div slot="header" class="clearfix">
                                          <span class="features" style="height: 46px;line-height: 46px;">评价：</span>
                                          <router-link :to="'/zc/edit/'+NanProgress.id">
                                            <el-button style="float: right;" class="features" type="text"><i class="el-icon-edit"></i></el-button>
                                          </router-link>
                                        </div>
                                        <span class="">&emsp;&emsp;{{ NanProgress.features }}</span>
                                    </el-card>
                                  </el-collapse-item>
                                </div>
                              </el-collapse>
                            </div>
                          </el-card>
                          </div>
            </el-main>
            <el-main>
                    <div class="right-container"  style="margin-left: 10%;padding-bottom: 20px;">
                            <el-card class="box-card-component" style="margin-left:8px;">
                              <div slot="header" class="box-card-header">
                                <img src="https://wpimg.wallstcn.com/e7d23d71-cf19-4b90-a1cc-f56af8c0903d.png">
                              </div>
                              <div style="position:relative;">
                                <pan-thumb :image="avatarNv" class="panThumb"/>
                                <mallki class-name="mallki-text" text="小懒猫-张凤姣"/>
                                <div style="padding-top:35px;" class="progress-item">
                                  <el-tag>属性分评</el-tag>
                                </div>
                                <el-collapse accordion>
                                  <div v-for="NvProgress in NvProgressList" class="progress-item">
                                    <el-collapse-item>
                                      <template slot="title">
                                        <span slot="reference">{{ NvProgress.attrname }}</span>
                                        <i class="header-icon el-icon-info"></i>
                                        <div style="display: inline;">
                                            <el-progress :percentage="NvProgress.progress" :status="NvProgress.status" 
                                            style="float: right;width: 70%;top:35%;"/>
                                        </div>
                                      </template>
                                      <el-card shadow="hover" class="box-card">
                                          <div slot="header" class="clearfix">
                                            <span class="features" style="height: 46px;line-height: 46px;">评价：</span>
                                            <router-link :to="'/zc/edit/'+NvProgress.id">
                                              <el-button style="float: right;" class="features" type="text"><i class="el-icon-edit"></i></el-button>
                                            </router-link>
                                          </div>
                                          <span class="">&emsp;&emsp;{{ NvProgress.features }}</span>
                                      </el-card>
                                    </el-collapse-item>
                                  </div>
                                </el-collapse>
                              </div>
                            </el-card>
                          </div>
            </el-main>
        </el-container>
        <el-footer>Footer</el-footer>
    </el-container>
</template>

<style scoped>
    .el-header, .el-footer {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
  }
  
  .el-aside {
    background-color: #D3DCE6;
    color: #333;
  }
  
  .el-main {
    background-color: #E9EEF3;
    color: #333;
  }
  
  body > .el-container {
    margin-bottom: 40px;
  }
</style>

<script>
        import { mapGetters } from 'vuex'
        import PanThumb from '@/components/PanThumb'
        import Mallki from '@/components/TextHoverEffect/Mallki'
        import splitPane from 'vue-splitpane'
        import { getAttributeList } from '@/api/zc'
        
        export default {
          name: 'SplitpaneDemo',
          components: { splitPane,PanThumb, Mallki },
          methods: {
            resize() {
              console.log('resize')
            },
            getNanProgressList() {
              var query = {'user': this.manId}
              getAttributeList(query).then(response => {
                this.NanProgressList = response.data.attrList
              })
            },
            getNvProgressList() {
              var query = {'user': this.menId}
              getAttributeList(query).then(response => {
                this.NvProgressList = response.data.attrList
              })
            }
          },
          created () {
            this.getNanProgressList()
            this.getNvProgressList()
          },
          data() {
            return {
              manId:1,// 男id  后期需要通过获取的方式获取用户id
              menId:2,// 女id
              statisticsData: {
                article_count: 1024,
                pageviews_count: 1024
              },
              avatarNan:"http://120.78.185.208/SecretHouse/NanZJ.jpg",
              avatarNv:"http://120.78.185.208/SecretHouse/NvZJ.jpg",
              NanProgressList:[{id:0,user_id:0,attrname:'无',progress: 0,status:'',features:''}],
              NvProgressList:[{id:0,user_id:0,attrname:'无',progress: 0,status:'',features:''}]
            }
          }
        }
        </script>
        
        <style  scoped>
          .components-container {
            position: relative;
            height: 128vh;
          }
        
          .left-container {
            /*background-color: #F38181;*/
            height: auto;
            width: 400px;
          }
        
          .right-container {
            /*background-color: #FCE38A;*/
            height: 100%;
            width: 400px;
          }
        
          .top-container {
            background-color: #FCE38A;
            width: 100%;
            height: 100%;
          }
        
          .bottom-container {
            width: 100%;
            background-color: #95E1D3;
            height: 100%;
          }
        
          .features {
            padding: 15px;
          }
        </style>

        <style>
        /*为了保证头像在白色半圆内*/
        .pan-thumb{
              left: 0px;
          }
        </style>
        
        <style rel="stylesheet/scss" lang="scss" >
        .box-card-component{
          .el-card__header {
            padding: 0px!important;
          }
        }
        </style>
        <style rel="stylesheet/scss" lang="scss" scoped>
        .box-card-component {
          .box-card-header {
            position: relative;
            height: 220px;
            img {
              width: 100%;
              height: 100%;
              transition: all 0.2s linear;
              &:hover {
                transform: scale(1.1, 1.1);
                filter: contrast(130%);
              }
            }
          }
          .mallki-text {
            position: absolute;
            top: 0px;
            right: 0px;
            font-size: 20px;
            font-weight: bold;
          }
          .panThumb {
            z-index: 100;
            height: 70px!important;
            width: 70px!important;
            position: absolute!important;
            top: -45px;
            left: 0px;
            border: 5px solid #ffffff;
            background-color: #fff;
            margin: auto;
            box-shadow: none!important;
            /deep/ .pan-info {
              box-shadow: none!important;
            }
          }
          .progress-item {
            margin-bottom: 10px;
            font-size: 14px;
          }
          @media only screen and (max-width: 1510px){
            .mallki-text{
              /*display: none;*/
            }
          }
        }
        </style>