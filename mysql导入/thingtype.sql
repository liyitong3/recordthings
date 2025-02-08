/*
 Navicat Premium Data Transfer

 Source Server         : 127.0.0.1
 Source Server Type    : MySQL
 Source Server Version : 50553
 Source Host           : 127.0.0.1:3306
 Source Schema         : memory_things_system

 Target Server Type    : MySQL
 Target Server Version : 50553
 File Encoding         : 65001

 Date: 07/02/2025 16:07:25
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for thingtype
-- ----------------------------
DROP TABLE IF EXISTS `thingtype`;
CREATE TABLE `thingtype`  (
  `id` int(2) NOT NULL,
  `leixing` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `beizhu` varchar(63) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL
) ENGINE = MyISAM CHARACTER SET = utf8mb4 COLLATE = utf8mb4_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of thingtype
-- ----------------------------
INSERT INTO `thingtype` VALUES (2, '实验室', '实验教学中心');
INSERT INTO `thingtype` VALUES (5, '监考', '各种监考');
INSERT INTO `thingtype` VALUES (4, '资产管理', '固定资产管理工作');
INSERT INTO `thingtype` VALUES (3, '领导交代', '无明确的岗位职责');
INSERT INTO `thingtype` VALUES (1, '个人记录', '个人事件记录和提醒');
INSERT INTO `thingtype` VALUES (6, '其它', '暂无明确分类');

SET FOREIGN_KEY_CHECKS = 1;
