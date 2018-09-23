<template>
  <div class="components-container">
    <code>
      个人属性一览表
    </code>
    <split-pane split="vertical" @resize="resize">
      <template slot="paneL">
        <div class="left-container">
          <el-card class="box-card-component" style="margin-left:8px;">
            <div slot="header" class="box-card-header">
              <img src="https://wpimg.wallstcn.com/e7d23d71-cf19-4b90-a1cc-f56af8c0903d.png">
            </div>
            <div style="position:relative;">
              <pan-thumb :image="avatar" class="panThumb"/>
              <mallki class-name="mallki-text" text="李小磊"/>
              <div style="padding-top:35px;" class="progress-item">
                <el-tag>属性分评</el-tag>
              </div>
              <div class="progress-item">
                <span>开朗</span>
                <el-progress :percentage="70"/>
              </div>
              <div class="progress-item">
                <span>可爱</span>
                <el-progress :percentage="18"/>
              </div>
              <div class="progress-item">
                <span>脾气</span>
                <el-progress :percentage="12"/>
              </div>
              <div class="progress-item">
                <span>评价</span>
                <el-progress :percentage="100" status="success"/>
              </div>
            </div>
          </el-card>
        </div>
      </template>
      <template slot="paneR">
        <div class="right-container">
          <el-card class="box-card-component" style="margin-left:8px;">
            <div slot="header" class="box-card-header">
              <img src="https://wpimg.wallstcn.com/e7d23d71-cf19-4b90-a1cc-f56af8c0903d.png">
            </div>
            <div style="position:relative;">
              <pan-thumb :image="avatar" class="panThumb"/>
              <mallki class-name="mallki-text" text="小懒猫-张凤姣"/>
              <div style="padding-top:35px;" class="progress-item">
                <el-tag>属性分评</el-tag>
              </div>
              <div class="progress-item">
                <span>开朗</span>
                <el-progress :percentage="70"/>
              </div>
              <div class="progress-item">
                <span>可爱</span>
                <el-progress :percentage="18"/>
              </div>
              <div class="progress-item">
                <span>脾气</span>
                <el-progress :percentage="12"/>
              </div>
              <div class="progress-item">
                <span>评价</span>
                <el-progress :percentage="100" status="success"/>
              </div>
            </div>
          </el-card>
        </div>
      </template>
    </split-pane>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import PanThumb from '@/components/PanThumb'
import Mallki from '@/components/TextHoverEffect/Mallki'
import splitPane from 'vue-splitpane'

export default {
  name: 'SplitpaneDemo',
  components: { splitPane,PanThumb, Mallki },
  methods: {
    resize() {
      console.log('resize')
    }
  },
  filters: {
    statusFilter(status) {
      const statusMap = {
        success: 'success',
        pending: 'danger'
      }
      return statusMap[status]
    }
  },
  data() {
    return {
      statisticsData: {
        article_count: 1024,
        pageviews_count: 1024
      }
    }
  },
  computed: {
    ...mapGetters([
      'name',
      'avatar',
      'roles'
    ])
  }
}
</script>

<style  scoped>
  .components-container {
    position: relative;
    height: 100vh;
  }

  .left-container {
    /*background-color: #F38181;*/
    height: 100%;
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
      display: none;
    }
  }
}
</style>