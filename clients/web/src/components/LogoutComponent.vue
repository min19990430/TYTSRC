<template>
    <div class="logout-container " @click="confirmLogout">
        <button @click="confirmLogout">
            <span class="material-symbols-outlined">
                logout
            </span>
        </button>
    </div>
</template>

<script>
import Swal from "sweetalert2";

export default {
    methods: {
        confirmLogout() {
            // 使用 SweetAlert2 顯示確認提示
            Swal.fire({
                title: "確定要登出嗎？",
                icon: "warning",
                showCancelButton: true,
                confirmButtonColor: "#3085d6",
                cancelButtonColor: "#d33",
                confirmButtonText: "是的, 我要登出",
                cancelButtonText: "取消",
            }).then((result) => {
                if (result.isConfirmed) {
                    // 如果使用者確認登出，執行登出動作
                    this.logout();
                }
            });
        },
        logout() {
            // 清除 sessionStorage 的登入資訊
            sessionStorage.clear();

            // 使用 SweetAlert2 顯示成功訊息
            Swal.fire({
                icon: "success",
                title: "已成功登出",
                showConfirmButton: false,
                timer: 1000,
            });

            // 在 1 秒後重新導向至登入頁面
            setTimeout(() => {
                this.$router.push("/login");
            }, 1000);
        },
    },
};
</script>
