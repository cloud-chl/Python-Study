import os
import sys
from utils.unlock_account import UnlockAccount
from utils.reset_password import ResetPassword
from utils.print_color import print_color_text, RED, GREEN


def main():
    try:
        action = sys.argv[1]
        if len(sys.argv) < 2:
            # sys.argv.append("manual")
            print_color_text(
                f"执行 {os.path.basename(__file__)} help 查看脚本使用方法", RED
            )

        if action == "help":
            print_color_text(
                f"Usage: {os.path.basename(__file__)} [ACTION] [OPTIONS]", GREEN
            )
            print_color_text(
                f"""
    reset: 重置产品默认密码, 支持: ras upm cas cmc
            {os.path.basename(__file__)} reset cas

        unlock: 解锁平台账户, 支持: ras upm cas cmc
        example:
            {os.path.basename(__file__)} unlock cas
    """,
                GREEN,
            )
            return

        elif action == "reset" or action == "unlock":
            # 产品名称
            product = sys.argv[2]

            if len(sys.argv) < 2:
                print_color_text(
                    f"""
    reset: 重置产品默认密码, 支持: ras upm cas cmc
        example:
            {os.path.basename(__file__)} reset cas

        unlock: 解锁平台账户, 支持: ras upm cas cmc
        example:
            {os.path.basename(__file__)} unlock cas
    """,
                    RED,
                )

            match (action, product):
                case ("unlock", "cas"):
                    UnlockAccount.cmc_and_cas("dblue")
                case ("unlock", "cmc"):
                    UnlockAccount.cmc_and_cas("cta-business-major")
                case ("unlock", "upm"):
                    UnlockAccount.upm()
                case ("unlock", "ras"):
                    UnlockAccount.ras()
                case ("reset", "cas"):
                    ResetPassword.cmc_and_cas("dblue")
                case ("reset", "cmc"):
                    ResetPassword.cmc_and_cas("cta-business-major")
                case ("reset", "upm"):
                    ResetPassword.upm()
                case ("reset", "ras"):
                    ResetPassword.ras()
                case _:
                    print_color_text(
                        f"无效的 action 或 product : {action} or {product}", RED
                    )
        else:
            print_color_text(f"无效的参数: {action}", RED)

    except Exception as e:
        return


if __name__ == "__main__":
    main()
