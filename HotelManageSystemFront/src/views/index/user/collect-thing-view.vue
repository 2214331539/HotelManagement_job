<!-- 查看收藏页面 -->

<template>
  <div class="content-list">
    <div class="list-title">我的收藏</div>
    <div role="tablist" class="list-tabs-view flex-view">
    </div>
    <div class="list-content">
      <div class="collect-thing-view">
        <a-spin :spinning="loading" style="min-height: 200px;">
          <div class="thing-list flex-view">
            <div class="thing-item item-column-3" v-for="(item, index) in pageData.collectData" :key="index">
              <div class="remove" @click="handleRemove(item)">移出</div>
              <div class="img-view" @click="handleClickItem(item)">
                <img :src="item.cover">
              </div>
              <p style="text-align: center;margin-top: 5px;font-weight: bold;">{{ item.title }}</p>
            </div>
            <template v-if="!pageData.collectData || pageData.collectData.length <= 0">
              <a-empty style="width: 100%;margin-top: 200px;" />
            </template>
          </div>
        </a-spin>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { message } from 'ant-design-vue';
import { getCollectThingListApi, removeCollectUserApi } from '/@/api/index/thing'
import { BASE_URL } from "/@/store/constants";
import { useUserStore } from "/@/store";

const router = useRouter();
const userStore = useUserStore();

const pageData = reactive({
  collectData: []
})

const loading = ref(false)

onMounted(() => {
  getCollectThingList()
})

const handleClickItem = (record) => {
  let text = router.resolve({ name: 'detail', query: { id: record.id } })
  window.open(text.href, '_blank')
}
const handleRemove = (record) => {
  let username = userStore.user_name
  removeCollectUserApi({ username: username, thingId: record.id }).then(res => {
    message.success('移除成功')
    getCollectThingList()
  }).catch(err => {
    console.log(err)
  })
}
const getCollectThingList = () => {
  loading.value = true
  let username = userStore.user_name
  getCollectThingListApi({ username: username }).then(res => {
    res.data.forEach(item => {
      item.cover = BASE_URL + item.cover
    })
    console.log(res.data)
    pageData.collectData = res.data
    loading.value = false
  }).catch(err => {
    console.log(err.msg)
    loading.value = false
  })
}

</script>
<style scoped lang="less">
.flex-view {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
}

.content-list {
  -webkit-box-flex: 1;
  -ms-flex: 1;
  flex: 1;

  .list-title {
    color: #152844;
    font-weight: 600;
    font-size: 18px;
    line-height: 24px;
    height: 24px;
    margin-bottom: 4px;
  }

  .list-tabs-view {
    position: relative;
    border-bottom: 1px solid #cedce4;
    height: 12px;
    line-height: 42px;
  }
}

.thing-list {
  -ms-flex-wrap: wrap;
  flex-wrap: wrap;
  -webkit-box-pack: start;
  -ms-flex-pack: start;
  justify-content: flex-start;

  .thing-item {
    position: relative;
    -webkit-box-flex: 1;
    -ms-flex: 1;
    flex: 1;
    margin-right: 20px;
    min-width: 255px;
    max-width: 255px;
    height: fit-content;
    border-radius: 4px;
    overflow: hidden;
    margin-top: 16px;
    cursor: pointer;

    .remove {
      position: absolute;
      right: 8px;
      top: 8px;
      width: 48px;
      height: 20px;
      text-align: center;
      line-height: 20px;
      color: #fff;
      background: #a1adc5;
      border-radius: 32px;
      cursor: pointer;
    }

    .img-view {
      background: #eaf1f5;
      font-size: 0;
      text-align: center;
      height: 156px;
      padding: 8px 0;

      img {
        max-width: 100%;
        height: 100%;
        display: block;
        margin: 0 auto;
        border-radius: 4px;
        -webkit-box-sizing: border-box;
        box-sizing: border-box;
      }
    }

    .info-view {
      background: #f6f9fb;
      text-align: center;
      height: 108px;
      overflow: hidden;
      padding: 0 16px;

      h3 {
        color: #1c355a;
        font-weight: 500;
        font-size: 16px;
        line-height: 20px;
        overflow: hidden;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;
        margin: 12px 0 8px;
      }

      .authors,
      .translators {
        color: #6f6f6f;
        font-size: 12px;
        line-height: 14px;
        margin-top: 4px;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
      }
    }
  }
}
</style>
