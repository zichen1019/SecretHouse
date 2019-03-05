import request from '@/utils/request'

// 查询今日待办事项
export function getTodayMustList(state) {
    console.log(state)
    return request({
        url: 'api/todaysMust/get',
        method: 'get',
        params: state
    });
}


// 删除今日必达事项
export function deleteTodaysMust(TodaysMustList) {
    return request({
        url: 'api/todaysMust/delete',
        method: 'post',
        data: TodaysMustList
    });
}