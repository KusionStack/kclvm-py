
import sys
import kclvm.kcl.error as kcl_error
import os

cwd = os.path.dirname(os.path.realpath(__file__))

kcl_error.print_kcl_error_message(
    kcl_error.get_exception(err_type=kcl_error.ErrType.SchemaCheckFailure_TYPE,
                            file_msgs=[
                                kcl_error.ErrFileMsg(
                                    filename=cwd + "/pkg/person.k",
                                    line_no=5,
                                    arg_msg=kcl_error.SCHEMA_CHECK_FILE_MSG_COND
                                ),
                                kcl_error.ErrFileMsg(
                                    filename=cwd + "/main.k",
                                    line_no=3,
                                    col_no=9,
                                    arg_msg=kcl_error.SCHEMA_CHECK_FILE_MSG_ERR
                                ),
                            ],
                            arg_msg="name should be defined")
    , file=sys.stdout
)

