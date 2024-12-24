import os
import requests
import ffmpeg

# 批量下载和转换 m3u8 文件
def download_and_convert_m3u8_to_mp4(files_list, output_dir='E:\output'):
    # 检查输出文件夹是否存在，不存在则创建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    isKeep = True
    

    for file_info in files_list:

        if isKeep == True:
            url = file_info['url']  # 下载的 m3u8 链接
            output_name = file_info['name']  # 导出的文件名
            isKeep = False
            os.system(f'ffmpeg -i "{url}" -c copy "E:\{output_name}.mp4"')
            isKeep = True
        # 下载 m3u8 文件
        # m3u8_response = requests.get(url)
        # m3u8_file = os.path.join(output_dir, f"{output_name}.m3u8")
        
        # with open(m3u8_file, 'wb') as f:
        #     f.write(m3u8_response.content)

        # 使用 ffmpeg 将 m3u8 转换为 mp4
        # output_file = os.path.join(output_dir, f"{output_name}.mp4")
        # (
        #     ffmpeg
        #     .input(m3u8_file)
        #     .output(output_file, codec='copy')  # 使用 copy 模式直接转码，不重新编码
        #     .run(overwrite_output=True)
        # )
        
        #print(f"Downloaded and converted: {output_name}.mp4")

# 示例：批量下载和转换文件
files_list = [
    {
        "url": "https://cloud-video.hkatv.vip/out/3069_1603961434_013296/index_1080p.m3u8?auth_key=1728739578-4287119564-0-b9a8a157f18ee70ed87ba17c781f2938",
        "name": "221"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3070_1603961432_079283/index_1080p.m3u8?auth_key=1728739581-939168452-0-581ee471a683e4e9979d8c0408484cb9",
        "name": "222"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3071_1603961430_373300/index_1080p.m3u8?auth_key=1728739584-446202073-0-cada35a89882a4267fa239c6d300987f",
        "name": "223"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3072_1603961425_597097/index_1080p.m3u8?auth_key=1728739587-2565424908-0-11c9c9a4b86d53c2331caaf8db2281a8",
        "name": "224"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3073_1603961424_893735/index_1080p.m3u8?auth_key=1728739591-3593782039-0-094d341d42d3bda2ac314153e8a2dc09",
        "name": "225"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3074_1603961421_218726/index_1080p.m3u8?auth_key=1728739595-4060577631-0-54d55d7ed35e1c616462522a0f34f15a",
        "name": "226"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3075_1603961420_724901/index_1080p.m3u8?auth_key=1728739599-2460300829-0-e340e57839919145e629a07ac1460380",
        "name": "227"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3076_1603961418_871209/index_1080p.m3u8?auth_key=1728739605-248582204-0-7cf856b35b1956709a1e9a029c098e29",
        "name": "228"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3077_1603961417_241500/index_1080p.m3u8?auth_key=1728739609-1513057051-0-97b0aefd295efe20af00ed959b69ec56",
        "name": "229"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3078_1603961415_321053/index_1080p.m3u8?auth_key=1728739614-4263170873-0-803703dad0f8656f162f060085b1232c",
        "name": "230"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3079_1603961413_638825/index_1080p.m3u8?auth_key=1728739618-2811958343-0-6fbaf62b5d3ff10381a16c9941f0a0e6",
        "name": "231"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3080_1603961412_539800/index_1080p.m3u8?auth_key=1728739621-1747757418-0-97bf6451d9995ce65a6df79853f5604d",
        "name": "232"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3081_1603961410_391006/index_1080p.m3u8?auth_key=1728739625-3644928583-0-3d2efb88cce8abe6a791df65ba3e471c",
        "name": "233"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3082_1603961408_283807/index_1080p.m3u8?auth_key=1728739630-3950982754-0-638cc67b91626a018a790d4c7b531cf3",
        "name": "234"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3083_1603961406_367020/index_1080p.m3u8?auth_key=1728739634-249318445-0-27cb7bc63f266b3b2a1a18ef8d05e127",
        "name": "235"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3084_1603961405_762970/index_1080p.m3u8?auth_key=1728739637-1339861234-0-026479c102f4997276a32f07de65149d",
        "name": "236"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3085_1603961402_081762/index_1080p.m3u8?auth_key=1728739642-4080007608-0-d122bfaccf855efed733b72869db302c",
        "name": "237"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3086_1603961400_882718/index_1080p.m3u8?auth_key=1728739647-352341487-0-fe5fb31961ebce59fbf6fa3070c496be",
        "name": "238"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3087_1603961395_336674/index_1080p.m3u8?auth_key=1728739650-1651112966-0-add5c2e6d147e6867dcf92db0cb115ae",
        "name": "239"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3088_1603961393_752159/index_1080p.m3u8?auth_key=1728739654-1302792325-0-dd95af4b9c8fe164272b2ed7925050aa",
        "name": "240"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3089_1603961391_710737/index_1080p.m3u8?auth_key=1728739657-2801072803-0-6208ac67138769d1e46b17d336491fa1",
        "name": "241"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3090_1603961390_493735/index_1080p.m3u8?auth_key=1728739662-1597116789-0-49d85f2e79710a75a14ffe24c17879cc",
        "name": "242"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3091_1603961388_233431/index_1080p.m3u8?auth_key=1728739669-3997590970-0-c727f577f9f43d29a12f3517c309f631",
        "name": "243"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3092_1603961386_468052/index_1080p.m3u8?auth_key=1728739676-3463100452-0-c232b54db673a10da749439cba6ac42f",
        "name": "244"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3093_1603961384_583445/index_1080p.m3u8?auth_key=1728739682-1158023054-0-6635d3721f972dcf31e24344621de962",
        "name": "245"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3094_1603961383_173400/index_1080p.m3u8?auth_key=1728739687-3266616424-0-78080219cb18de1e3bd5a66bb050f1f1",
        "name": "246"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3095_1603961381_795864/index_1080p.m3u8?auth_key=1728739696-946054289-0-c21ee3e53031f0fd1a650d5a0452be30",
        "name": "247"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3096_1603961379_971797/index_1080p.m3u8?auth_key=1728739700-2602093876-0-51aba98bb810574f869d1defd315ae61",
        "name": "248"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3097_1603961377_544022/index_1080p.m3u8?auth_key=1728739706-2109718461-0-5dc068f24f679bc774c413cc00a98a4c",
        "name": "249"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3098_1603961375_823626/index_1080p.m3u8?auth_key=1728739712-574457771-0-5d85b59a1858b55036e68caaef54969a",
        "name": "250"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3099_1603961374_700381/index_1080p.m3u8?auth_key=1728739717-2085377740-0-f942ddc06aa363217a61a15b0ad5f0b2",
        "name": "251"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3100_1603961372_179978/index_1080p.m3u8?auth_key=1728739724-2683685784-0-e68e5bad32ddf39a8ca4b64204b93f27",
        "name": "252"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3101_1603961370_474127/index_1080p.m3u8?auth_key=1728739731-2627173623-0-4b055c103eca362fcc217a7c7ff09a25",
        "name": "253"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3102_1603961366_948698/index_1080p.m3u8?auth_key=1728739739-4228990526-0-eea1bbfb29d5aa6533d4865dea550e66",
        "name": "254"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3103_1603961364_604571/index_1080p.m3u8?auth_key=1728739745-1582377558-0-252a4f9bf56232900bb81b1c906e4910",
        "name": "255"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3104_1603961363_663825/index_1080p.m3u8?auth_key=1728739750-2800803295-0-39eb0ba38b95efb70e90f40b3458885a",
        "name": "256"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3105_1603961361_462546/index_1080p.m3u8?auth_key=1728739756-3616123874-0-d0b2e5128d3f5e7c3a53703841ea8f1a",
        "name": "257"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3106_1603961360_619536/index_1080p.m3u8?auth_key=1728739762-3025144135-0-62b58bdc20d55b136babf6aa3410da00",
        "name": "258"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3107_1603961358_778957/index_1080p.m3u8?auth_key=1728739768-3778141140-0-84baa3a173cab00ad9c19e6f4be41809",
        "name": "259"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3108_1603961356_709970/index_1080p.m3u8?auth_key=1728739773-1725736843-0-edbb2c8267d3299b15a7644f6179716c",
        "name": "260"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3109_1603961355_338581/index_1080p.m3u8?auth_key=1728739777-1188974974-0-e93986304732cca220a05d99eae12b1b",
        "name": "261"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3110_1603961353_097813/index_1080p.m3u8?auth_key=1728739782-2230887275-0-a20f9ae3ea8f604a61903a2bda2b7b6f",
        "name": "262"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3111_1603961351_893762/index_1080p.m3u8?auth_key=1728739787-3011322463-0-219b46a08b4b8370b1660a4e23ede5d5",
        "name": "263"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3112_1603961349_805191/index_1080p.m3u8?auth_key=1728739792-1892004551-0-6d1e5a24d2d5a5de8bfe422e2311b582",
        "name": "264"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3113_1603961348_469717/index_1080p.m3u8?auth_key=1728739798-1220599442-0-dcc23b28441a9c46e5bc4235bb6401a5",
        "name": "265"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3114_1603961346_288007/index_1080p.m3u8?auth_key=1728739806-1086790822-0-61de6908ad8eed81d344ee21c90dfcd8",
        "name": "266"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3115_1603961344_453122/index_1080p.m3u8?auth_key=1728739813-2029373245-0-f3593b37b65438c4febfe346ac936f0b",
        "name": "267"
    },
    {
        "url": "https://cloud-video.hkatv.vip/out/3116_1603961342_784647/index_1080p.m3u8?auth_key=1728739818-585978540-0-d2771a48ded163d9d6fb2b4e114a4e43",
        "name": "268"
    }
]
download_and_convert_m3u8_to_mp4(files_list)
