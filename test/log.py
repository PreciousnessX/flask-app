import logging

if __name__ == "__main__":
    # 日志记录最低输出级别设置
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Logging记录到文件
    fh = logging.FileHandler("test.log", mode='w')
    logger.addHandler(fh)  # 将logger添加到handler里面

    # Logging记录格式以及设置
    formatter = logging.Formatter("%(asctime)s - %(message)s")  # 记录时间和消息
    fh.setFormatter(formatter)  # 此处设置handler的输出格式

    # Logging使用
    logger.info("this is info")
    logger.debug("this is debug")
    logger.warning("this is warning")
    logging.error("this is error")
    logger.critical("this is critical")
