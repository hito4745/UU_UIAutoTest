import json
import sys
import time
from time import sleep
from playwright.async_api import Dialog
from seldom.testdata.conversion import json_to_list
from page.inventory_page import InventoryPage
import allure
import pytest
from common.config import *
from playwright.sync_api import Playwright, sync_playwright, expect


class TestHomePage:

    def test_homepage(self, logged_page):
        print("已登录")
